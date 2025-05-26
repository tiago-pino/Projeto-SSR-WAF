# waf.py (Phase 3: Basic Pattern Matching)
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json # For loading the configuration file
import os   # For checking if config file exists
from urllib.parse import urlparse, parse_qs # For parsing URL paths and query strings

# --- Configuration Loading ---
CONFIG_FILE = 'config.json'
CONFIG = {}
LISTEN_PORT = 8080

def load_config():
    global CONFIG
    # Default configuration in case the file is missing or malformed
    default_config = {
        "blocked_domains": [],
        "blocked_ips": [],
        "blocked_paths_for_all_domains": [],
        "blocked_paths_for_specific_domain": {},
        "log_level": "INFO",
        "suspicious_query_patterns": [],
        "blocked_user_agents": []
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                CONFIG = json.load(f)
            # Ensure all expected keys have defaults if missing in the loaded config
            for key, value in default_config.items():
                CONFIG.setdefault(key, value)
            print(f"Configuration successfully loaded from {CONFIG_FILE}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {CONFIG_FILE}: {e}. Using default configuration.")
            CONFIG = default_config
        except Exception as e:
            print(f"Error loading configuration from {CONFIG_FILE}: {e}. Using default configuration.")
            CONFIG = default_config
    else:
        print(f"Warning: {CONFIG_FILE} not found. Using default configuration.")
        CONFIG = default_config

# --- WAF Request Handler ---
class WAFRequestHandler(BaseHTTPRequestHandler):
    
    def send_block_response(self, reason_message="Access Denied by WAF"):
        """Helper function to send a 403 Forbidden response."""
        # Log the block with client IP, host, and full path
        client_ip_for_log = self.client_address[0]
        host_for_log = self.headers.get('Host', 'N/A')
        path_for_log = self.path # self.path contains the full URL for proxy requests

        print(f"--- Blocking request: {reason_message} (Client: {client_ip_for_log}, Host: {host_for_log}, Path: {path_for_log}) ---")
        
        self.send_response(403)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>403 Forbidden: Access Denied by WAF</h1>")
        self.wfile.write(f"<p>{reason_message}</p>".encode())

    def do_GET(self):
        client_ip = self.client_address[0]
        target_host = self.headers.get('Host') # Original Host header from client
        
        # Use urlparse to reliably get the path and query components
        # self.path from BaseHTTPRequestHandler for a proxy request is the full URL (e.g., "http://example.com/page?query=1")
        parsed_url = urlparse(self.path)
        actual_path_for_rules = parsed_url.path # e.g., "/page"
        query_params = parse_qs(parsed_url.query) # e.g., {'query': ['1']}

        # Logging request details
        print(f"--- Request Received ---")
        print(f"Client IP: {client_ip}")
        print(f"Method: {self.command}")
        print(f"Target Host Header: {target_host}") # Host header sent by client
        print(f"Full Request Line (self.path): {self.path}")
        print(f"Path for Rules (parsed_url.path): {actual_path_for_rules}")
        print(f"Query Parameters: {query_params}")

        # --- Rule Checks ---
        # 1. Check IP Blocklist
        if client_ip in CONFIG.get("blocked_ips", []):
            self.send_block_response(f"IP address {client_ip} is blocked.")
            return

        if not target_host:
            self.send_block_response("Bad Request: Host header missing in original request.")
            return

        # 2. Check Domain Blocklist (based on Host header)
        if target_host in CONFIG.get("blocked_domains", []):
            self.send_block_response(f"Domain '{target_host}' is blocked.")
            return

        # 3. Check Blocked Paths (for all domains)
        if actual_path_for_rules in CONFIG.get("blocked_paths_for_all_domains", []):
            self.send_block_response(f"Path '{actual_path_for_rules}' is blocked for all domains.")
            return

        # 4. Check Blocked Paths (for specific domain)
        domain_specific_blocked_paths = CONFIG.get("blocked_paths_for_specific_domain", {}).get(target_host, [])
        if actual_path_for_rules in domain_specific_blocked_paths:
            self.send_block_response(f"Path '{actual_path_for_rules}' is blocked for domain '{target_host}'.")
            return

        # 5. Check Blocked User-Agents (Phase 3)
        user_agent = self.headers.get('User-Agent', '')
        for blocked_ua_pattern in CONFIG.get("blocked_user_agents", []):
            # Using "in" for partial match, "==" for exact match.
            # For this example we use exact match
            if blocked_ua_pattern == user_agent: 
                self.send_block_response(f"User-Agent '{user_agent}' is blocked.")
                return
            # For partial match:
            # if blocked_ua_pattern.lower() in user_agent.lower():
            #     self.send_block_response(f"User-Agent containing '{blocked_ua_pattern}' is blocked (Full UA: '{user_agent}').")
            #     return

        # 6. Check Suspicious Query Parameter Patterns
        for param_name, param_values_list in query_params.items():
            for value_str in param_values_list: # param_values_list is a list of strings
                for pattern in CONFIG.get("suspicious_query_patterns", []):
                    # Simple substring check. For case-insensitivity: pattern.lower() in value_str.lower()
                    if pattern in value_str:
                        self.send_block_response(f"Suspicious pattern '{pattern}' found in query parameter '{param_name}'. Value: '{value_str}'")
                        return
        # --- End Rule Checks ---

        # If not blocked, forward the request
        # The target_url for requests.get() should be the full URL from self.path
        target_url_for_forwarding = self.path 
        print(f"--- Forwarding request to: {target_url_for_forwarding} (Original Host Header was: {target_host}) ---")
        
        try:
            # Prepare headers for the outgoing request:
            # - Remove 'Host' because 'requests' will set it based on target_url_for_forwarding's netloc.
            # - Remove other hop-by-hop headers not suitable for forwarding.
            forward_headers = {key: value for key, value in self.headers.items()
                               if key.lower() not in ['host', 'proxy-connection', 'connection', 'keep-alive']}

            # Ensure the target URL is HTTP (this WAF version doesn't handle HTTPS forwarding)
            if not target_url_for_forwarding.lower().startswith("http://"):
                self.send_block_response("Bad Request: This WAF only forwards http:// URLs.")
                return

            # Using timeout for requests.get
            resp = requests.get(target_url_for_forwarding, headers=forward_headers, allow_redirects=False, timeout=10)

            self.send_response(resp.status_code)
            
            # Relay relevant headers from the target server's response back to the client
            # Skip hop-by-hop headers and headers that will be managed by this proxy or `requests`
            skipped_headers_debug = [] 
            sent_headers_debug = {}    

            for key, value in resp.headers.items():
                l_key = key.lower()
                # If `requests` decompresses content (default without stream=True), don't send original Content-Encoding.
                # Our current forwarding logic (using resp.content) means requests decompresses.
                if l_key == 'content-encoding': 
                    skipped_headers_debug.append(f"Skipping original Content-Encoding header: {value}")
                    continue 
                # Transfer-Encoding is hop-by-hop.
                if l_key == 'transfer-encoding':
                    skipped_headers_debug.append(f"Skipping original Transfer-Encoding header: {value}")
                    continue
                # We will set our own Content-Length based on resp.content.
                if l_key == 'content-length':
                    skipped_headers_debug.append(f"Skipping original Content-Length header: {value}")
                    continue
                # Other common hop-by-hop headers
                if l_key in ['connection', 'proxy-authenticate', 'proxy-authorization', 'te', 'trailers', 'upgrade', 'keep-alive']:
                    skipped_headers_debug.append(f"Skipping hop-by-hop header: {key}")
                    continue
                
                self.send_header(key, value)
                sent_headers_debug[key] = value
            
            body_bytes = resp.content # This gets the full body, decompressed by `requests`
            self.send_header('Content-Length', str(len(body_bytes)))
            sent_headers_debug['Content-Length'] = str(len(body_bytes))

            # For debugging header handling:
            # print(f"DEBUG: Skipped response headers: {skipped_headers_debug}")
            # print(f"DEBUG: Sent response headers: {sent_headers_debug}")

            self.end_headers()
            self.wfile.write(body_bytes)

        except requests.exceptions.Timeout:
            print(f"Timeout error forwarding request for {target_url_for_forwarding}")
            self.send_block_response(f"Gateway Timeout: Could not connect to {target_host if target_host else 'the target server'} in time.")
        except requests.exceptions.RequestException as e:
            print(f"Error forwarding request for {target_url_for_forwarding}: {e}")
            self.send_block_response(f"Bad Gateway: Could not connect to {target_host if target_host else 'the target server'}")
        except Exception as e_general:
            print(f"General error during forwarding for {target_url_for_forwarding}: {e_general}")
            self.send_block_response("Internal Server Error while proxying")

    def do_POST(self):
        client_ip = self.client_address[0]
        target_host = self.headers.get('Host')
        print(f"--- POST Request Received --- Client IP: {client_ip}, Host: {target_host}, Path: {self.path}")

        # Apply IP and User-Agent blocking for POST as well
        if client_ip in CONFIG.get("blocked_ips", []):
            self.send_block_response(f"IP address {client_ip} is blocked (POST).")
            return
        
        user_agent = self.headers.get('User-Agent', '')
        for blocked_ua in CONFIG.get("blocked_user_agents", []):
            if blocked_ua == user_agent: # Exact match
                self.send_block_response(f"User-Agent '{user_agent}' is blocked (POST).")
                return
        
        # POST body inspection and forwarding is more complex.
        # For now, block POSTs that haven't been IP/UA blocked.
        self.send_block_response("POST requests are not fully processed by this WAF version.")

    def do_HEAD(self):
        client_ip = self.client_address[0]
        target_host = self.headers.get('Host')
        print(f"--- HEAD Request Received --- Client IP: {client_ip}, Host: {target_host}, Path: {self.path}")

        # Apply IP and User-Agent blocking for HEAD
        if client_ip in CONFIG.get("blocked_ips", []):
            self.send_block_response(f"IP address {client_ip} is blocked (HEAD).")
            return

        user_agent = self.headers.get('User-Agent', '')
        for blocked_ua in CONFIG.get("blocked_user_agents", []):
            if blocked_ua == user_agent: # Exact match
                self.send_block_response(f"User-Agent '{user_agent}' is blocked (HEAD).")
                return
        
        # HEAD request forwarding would involve making a GET, getting headers, but not body.
        # For simplicity, we can block them if not IP/UA blocked.
        self.send_block_response("HEAD requests are not fully processed by this WAF version.")

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except ConnectionResetError:
            # This can happen if the client closes the connection abruptly
            print(f"Connection reset by client: {self.client_address}")
        except Exception as e:
            # Catch-all for other errors during request handling by http.server
            # self.command might not be set if error is very early
            command_attr = getattr(self, 'command', 'Unknown Command')
            path_attr = getattr(self, 'path', 'Unknown Path')
            client_addr_attr = getattr(self, 'client_address', ('Unknown IP', 0))

            if command_attr not in ['GET', 'POST', 'HEAD']:
                print(f"--- {command_attr} Request Received --- Client IP: {client_addr_attr[0]}, Path: {path_attr}")
                # Try to send a block response if possible
                if not getattr(self.wfile, 'closed', True): # Check if wfile is available and not closed
                    try:
                        self.send_block_response(f"Unsupported method ('{command_attr}')")
                    except Exception as e_send:
                        print(f"Error sending block response for unsupported method: {e_send}")
                else:
                    print("wfile closed, cannot send block response for unsupported method.")
            else:
                # For errors within implemented methods that weren't caught by their own try-except
                print(f"Unhandled exception in request handling for {command_attr} {path_attr}: {e}")
                if not getattr(self.wfile, 'closed', True):
                    try:
                        self.send_block_response("Internal Server Error during request processing")
                    except Exception as e_send_final:
                        print(f"Error sending final Internal Server Error response: {e_send_final}")
    
    # Suppress default http.server logging to avoid duplicate log lines with our custom prints
    def log_message(self, format, *args):
        # Enable this for the default logging format,
        # but it might be redundant with the custom print statements.
        # super().log_message(format, *args)
        pass

# --- Main WAF Runner ---
def run_waf(server_class=HTTPServer, handler_class=WAFRequestHandler, port=LISTEN_PORT):
    print("--- RUN_WAF FUNCTION CALLED (WAF Startup Sequence) ---") 
    
    load_config() # Load configuration at startup
    print(f"--- CONFIGURATION LOADED (Blocked IPs: {CONFIG.get('blocked_ips')}) ---")
    
    actual_port = CONFIG.get("listen_port", port) 
    print(f"--- WAF WILL LISTEN ON PORT: {actual_port} ---")

    server_address = ('', actual_port) 
    httpd = server_class(server_address, handler_class)
    print(f"Starting WAF on port {actual_port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping WAF (KeyboardInterrupt).")
    except Exception as e:
        print(f"WAF server error: {e}")
    finally:
        httpd.server_close()
        print("WAF server stopped.")

if __name__ == '__main__':
    run_waf()
