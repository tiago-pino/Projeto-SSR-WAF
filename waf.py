TiagoP
tiagopino
Disponível

TiagoP — 09/03/2025, 14:16
https://prod.liveshare.vsengsaas.visualstudio.com/join?AC97673CC07004B35549D6FBEECDD9A0E2D3
Visual Studio Code for the Web
Build with Visual Studio Code, anywhere, anytime, entirely in your browser.
https://prod.liveshare.vsengsaas.visualstudio.com/join?779AC78FA96A63D26490CA5B4D750294EF27
Visual Studio Code for the Web
Build with Visual Studio Code, anywhere, anytime, entirely in your browser.
Xixo — 09/03/2025, 14:33
https://prod.liveshare.vsengsaas.visualstudio.com/join?9F736009505D34B337C216FC5B9C2E993911
Visual Studio Code for the Web
Build with Visual Studio Code, anywhere, anytime, entirely in your browser.
TiagoP — 09/03/2025, 14:40
tiagopino12@gmail.com
TiagoP — 09/03/2025, 15:15
https://pt.overleaf.com/2623769184gjwzvwffqrsh#f8abe6
Overleaf, Editor LaTeX Online
Um editor de LaTeX online fácil de usar. Sem instalação, colaboração em tempo real, controle de versões, centenas de templates LaTeX e mais.
Imagem
TiagoP — 10/03/2025, 17:23
Acrescentei varias coisas ao relatório na parde da DCT. Desde da transformação DCT2 onde se obtem os coeficientes depois usar isso para ver o numereo de coeficientes e depois ainda estava atentar obter a transformada inversa dependendo da energia para ver os resultados. Taambém acrescentei funções no código (estão no fundo da célula das funções) para esses efeitos. Na transformada inversa estou com um problema de tamanhos por causa das imagens não serem quadradas. Temos de resolver isso (colocar zeros) e depois ver se o processo funcionou. Com isso o 2.1 está praticamente feito
As chamadas ás funções estão no fundo
Xixo — 10/03/2025, 19:44
Top
Depois analiso quando tiver tempo
Eu também acabei a parte da wavelet no relatório, não sei se viste
TiagoP — 10/03/2025, 19:46
Pareceu-me que ía  bem. Sendo assim é acabar a questão da reconstrução e fazer a última parte. Quanto ao SSIM queria perguntar à professora se é realmente para escolher apenas 1
Xixo — 10/03/2025, 19:59
É isso
Eu tenho quase a certeza que é, mas sim na dúvida é melhor perguntar
Xixo
 iniciou uma chamada que durou uma hora. — 16/04/2025, 16:20
Xixo — 16/04/2025, 17:09
Destination Address: While the RFC explicitly states HELLO messages are "broadcast", it doesn't specify the exact destination IP address used for the UDP/IP encapsulation within the RFC itself. However, the standard mechanism in IPv4 for a broadcast that is limited to the local link (which aligns with TTL=1 and the purpose of HELLO messages) is the limited broadcast address.
Constraint: The question specifies that the Ipv4Broadcast configuration is not set. This implies we should use the default or standard behavior. The standard default for a local, non-configurable broadcast in IPv4 is 255.255.255.255.
TiagoP — 16/04/2025, 17:22
https://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml
Xixo
 iniciou uma chamada que durou uma hora. — Ontem às 12:35
Xixo — Ontem às 12:41
https://aistudio.google.com/prompts/1rBJjrFTbnytIO4Iy5fkK11YVn7hbRGmU
Sign in - Google Accounts
https://aistudio.google.com/prompts/1KPnDwv0nG7F0FN7BqBtA_PeWtrZZDihL
Sign in - Google Accounts
https://aistudio.google.com/prompts/1RdTdheCheJEZ5weu6bvJRO-p4C0HNxab
Sign in - Google Accounts
# waf.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests # For making HTTP requests to the actual target server

# --- Configuration ---
LISTEN_PORT = 8080
Expandir
message.txt
4 KB
Você perdeu uma chamada de 
Xixo
 que durou poucos segundos. — Ontem às 13:59
Xixo — Ontem às 14:03
?
TiagoP
 iniciou uma chamada que durou 10 horas. — Ontem às 14:08
Xixo — Ontem às 15:08
docker-compose.yml,
version: '3.8' # Specifies the version of the Docker Compose file format

services:
  waf: # This is the name of our service (our WAF container)
    build:
      context: . # Tells Docker Compose to build the image using the Dockerfile in the current directory (.)
      # The 'memory' key here is likely not supported for 'build' in your Docker version (19.03.8)
      # We will try setting memory with 'docker build' command directly if needed.
    ports:
      
"8080:8080" # Maps port 8080 on your computer (host) to port 8080 inside the WAF container# Format is "HOST_PORT:CONTAINER_PORT"
  dns:
8.8.8.8
1.1.1.1,
# For development, you might want to mount your code directly into the container# so you don't have to rebuild the image for every code change:
volumes:
./waf.py:/app/waf.py
./requirements.txt:/app/requirements.txt,
,
#   # If you add a config.json later for Phase 2:#   # - ./config.json:/app/config.json,
,
# docker-compose.yml
version: '3.8' # Specifies the version of the Docker Compose file format

services:
  waf: # This is the name of our service (our WAF container)
    build:
Expandir
docker-compose.yml
2 KB
Tipo de arquivo em anexo: unknown
Dockerfile
1.83 KB
# requirements.txt
requests
requirements.txt
1 KB
Xixo — Ontem às 15:38
docker-compose build --no-cache waf
Imagem
TiagoP — Ontem às 16:37
docker-compose build --no-cache waf
Building waf
Step 1/13 : FROM python:3.9-bookworm
 ---> f1a1f81b5871
Step 2/13 : ARG DEBIAN_KEYRING_PKG_FILENAME=debian-archive-keyring_2023.3+deb12u2_all.deb
 ---> Running in 38c00fb14225
Removing intermediate container 38c00fb14225
 ---> f7bd6d8e81f6
Step 3/13 : ARG DEBIAN_KEYRING_PKG_URL=http://ftp.debian.org/debian/pool/main/d/debian-archive-keyring/$%7BDEBIAN_KEYRING_PKG_FILENAME%7D
 ---> Running in 71e1392e0889
Removing intermediate container 71e1392e0889
 ---> f37204179c83
Step 4/13 : ADD ${DEBIAN_KEYRING_PKG_URL} /tmp/${DEBIAN_KEYRING_PKG_FILENAME}

 ---> e56dcac44a2f
Step 5/13 : RUN echo "Attempting to install debian-archive-keyring with dpkg..." &&     dpkg -i /tmp/${DEBIAN_KEYRING_PKG_FILENAME} &&     rm /tmp/${DEBIAN_KEYRING_PKG_FILENAME} &&     echo "debian-archive-keyring installation via dpkg attempted."
 ---> Running in 9984c1010eca
Attempting to install debian-archive-keyring with dpkg...
dpkg-deb (subprocess): decompressing archive '/tmp/debian-archive-keyring_2023.3+deb12u2_all.deb' (size=178572) member 'control.tar': lzma error: Cannot allocate memory
tar: This does not look like a tar archive
tar: Exiting with failure status due to previous errors
dpkg-deb: error: tar subprocess returned error exit status 2
dpkg: error processing archive /tmp/debian-archive-keyring_2023.3+deb12u2_all.deb (--install):
 dpkg-deb --control subprocess returned error exit status 2
Errors were encountered while processing:
 /tmp/debian-archive-keyring_2023.3+deb12u2_all.deb
ERROR: Service 'waf' failed to build : The command '/bin/sh -c echo "Attempting to install debian-archive-keyring with dpkg..." &&     dpkg -i /tmp/${DEBIAN_KEYRING_PKG_FILENAME} &&     rm /tmp/${DEBIAN_KEYRING_PKG_FILENAME} &&     echo "debian-archive-keyring installation via dpkg attempted."' returned a non-zero code: 1
Xixo — Ontem às 16:42
FROM python:3.9-bookworm

ARG DEBIAN_KEYRING_PKG_FILENAME=debian-archive-keyring_2023.3+deb12u2_all.deb
ARG DEBIAN_KEYRING_PKG_URL=http://ftp.debian.org/debian/pool/main/d/debian-archive-keyring/$%7BDEBIAN_KEYRING_PKG_FILENAME%7D

Update package lists and upgrade system packages first,
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends --download-only ca-certificates && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*

Then proceed with your keyring installation,
ADD ${DEBIAN_KEYRING_PKG_URL} /tmp/${DEBIAN_KEYRING_PKG_FILENAME}
RUN echo "Attempting to install debian-archive-keyring with dpkg..." && \
    dpkg -i /tmp/${DEBIAN_KEYRING_PKG_FILENAME} && \
    rm /tmp/${DEBIAN_KEYRING_PKG_FILENAME} && \
    echo "debian-archive-keyring installation via dpkg attempted." && \
    apt-get update # Update again after adding new keyring
... rest of your Dockerfile,
FROM python:3.9-bookworm

ARG DEBIAN_KEYRING_PKG_FILENAME=debian-archive-keyring_2023.3+deb12u2_all.deb
ARG DEBIAN_KEYRING_PKG_URL=http://ftp.debian.org/debian/pool/main/d/debian-archive-keyring/${DEBIAN_KEYRING_PKG_FILENAME}

# Update package lists and upgrade system packages first
Expandir
1.txt
1 KB
apt-get install -y --reinstall debian-archive-keyring && \
TiagoP — Ontem às 16:46
docker-compose build --no-cache waf
Building waf
Step 1/14 : FROM python:3.9-bookworm
 ---> f1a1f81b5871
Step 2/14 : ARG DEBIAN_KEYRING_PKG_FILENAME=debian-archive-keyring_2023.3+deb12u2_all.deb
 ---> Running in 5017a52091a7
Removing intermediate container 5017a52091a7
 ---> 0cc9b1c73990
Step 3/14 : ARG DEBIAN_KEYRING_PKG_URL=http://ftp.debian.org/debian/pool/main/d/debian-archive-keyring/$%7BDEBIAN_KEYRING_PKG_FILENAME%7D
 ---> Running in abc12d1df977
Removing intermediate container abc12d1df977
 ---> d5cb3241ca5f
Step 4/14 : RUN apt-get update &&     apt-get install -y --reinstall debian-archive-keyring &&     apt-get upgrade -y &&     apt-get install --no-install-recommends --download-only ca-certificates &&     apt-get install -y ca-certificates &&     rm -rf /var/lib/apt/lists/*
 ---> Running in a7081f0fa46f
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Err:1 http://deb.debian.org/debian bookworm InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 0E98404D386FA1D9 NO_PUBKEY 6ED0E7B82643E131 NO_PUBKEY F8D2585B8783D481
Err:2 http://deb.debian.org/debian bookworm-updates InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 0E98404D386FA1D9 NO_PUBKEY 6ED0E7B82643E131
Err:3 http://deb.debian.org/debian-security bookworm-security InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 54404762BBB6E853 NO_PUBKEY BDE6D2B9216EC7A8
Reading package lists...
W: GPG error: http://deb.debian.org/debian bookworm InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 0E98404D386FA1D9 NO_PUBKEY 6ED0E7B82643E131 NO_PUBKEY F8D2585B8783D481
E: The repository 'http://deb.debian.org/debian bookworm InRelease' is not signed.
W: GPG error: http://deb.debian.org/debian bookworm-updates InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 0E98404D386FA1D9 NO_PUBKEY 6ED0E7B82643E131
E: The repository 'http://deb.debian.org/debian bookworm-updates InRelease' is not signed.
W: GPG error: http://deb.debian.org/debian-security bookworm-security InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 54404762BBB6E853 NO_PUBKEY BDE6D2B9216EC7A8
E: The repository 'http://deb.debian.org/debian-security bookworm-security InRelease' is not signed.
E: Problem executing scripts APT::Update::Post-Invoke 'rm -f /var/cache/apt/archives/.deb /var/cache/apt/archives/partial/.deb /var/cache/apt/.bin || true'
E: Sub-process returned an error code
ERROR: Service 'waf' failed to build : The command '/bin/sh -c apt-get update &&     apt-get install -y --reinstall debian-archive-keyring &&     apt-get upgrade -y &&     apt-get install --no-install-recommends --download-only ca-certificates &&     apt-get install -y ca-certificates &&     rm -rf /var/lib/apt/lists/' returned a non-zero code: 100
Xixo — Ontem às 18:22
# docker-compose.yml
version: '3.8' # Specifies the version of the Docker Compose file format

services:
  waf: # This is the name of our service (our WAF container)
    build:
Expandir
docker-compose.yml
2 KB
Tipo de arquivo em anexo: unknown
Dockerfile
1.83 KB
# requirements.txt
requests
requirements.txt
1 KB
# waf.py (Revised for simpler decompression handling)
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

LISTEN_PORT = 8080
BLOCKED_DOMAINS = ["example-blocked.com", "another-blocked-site.org"]
Expandir
waf.py
6 KB
Xixo — Ontem às 20:22
Imagem
Imagem
Imagem
Imagem
Xixo — Ontem às 20:56
Imagem
Imagem
# waf.py (Phase 2 Modifications)
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json # For loading the configuration file
import os   # For checking if config file exists
from urllib.parse import urlparse # For parsing URL paths
Expandir
waf(.py).txt
11 KB
{
  "blocked_domains": [
    "example-blocked.com",
    "another-blocked-site.org"
  ],
  "blocked_ips": [
Expandir
config(.json).txt
1 KB
# docker-compose.yml
version: '3.8' # Specifies the version of the Docker Compose file format

services:
   waf:
     build:
Expandir
docker-compose(.yml).txt
1 KB
# Dockerfile

# 1. Start with an official Python base image.
FROM python:3.9-bookworm
ENV PYTHONUNBUFFERED=1
Expandir
Dockerfile.txt
2 KB
# requirements.txt
requests
requirements.txt
1 KB
Xixo — Ontem às 23:19
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
TiagoP — Ontem às 23:37
d
Xixo — Ontem às 23:37
{
  "blocked_domains": [
    "example-blocked.com",
    "another-blocked-site.org"
  ],
  "blocked_ips": [
Expandir
config(.json).txt
1 KB
{
  "blocked_domains": [
    "example-blocked.com",
    "another-blocked-site.org"
  ],
  "blocked_ips": [
Expandir
config_ip(.json).txt
1 KB
# docker-compose.yml
version: '3.8' # Specifies the version of the Docker Compose file format

services:
   waf:
     build:
Expandir
docker-compose(.yml).txt
1 KB
# Dockerfile

# 1. Start with an official Python base image.
FROM python:3.9-bookworm
ENV PYTHONUNBUFFERED=1
Expandir
Dockerfile.txt
2 KB
# requirements.txt
requests
requirements.txt
1 KB
# waf.py (Phase 2 Modifications)
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json # For loading the configuration file
import os   # For checking if config file exists
from urllib.parse import urlparse # For parsing URL paths
Expandir
waf(.py).txt
11 KB
Xixo — Ontem às 23:45
Tipo de arquivo em anexo: acrobat
Web Application Security.pdf
5.10 MB
Tipo de arquivo em anexo: acrobat
Wenliang Du - Computer & Internet Security_ A Hands-on Approach (2019, Wenliang Du) - libgen.li [386-409].pdf
8.35 MB
Tipo de arquivo em anexo: acrobat
000017313.pdf
4.62 MB
Tipo de arquivo em anexo: acrobat
WEBAPP~2.PDF
6.89 MB
TiagoP — Ontem às 23:47
https://pt.overleaf.com/4749222679gjpjdghhwmyn#7e1514
Overleaf, Editor LaTeX Online
Um editor de LaTeX online fácil de usar. Sem instalação, colaboração em tempo real, controle de versões, centenas de templates LaTeX e mais.
Imagem
Xixo
 fixou uma mensagem neste canal. Ver todas as mensagens fixadas. — Ontem às 23:47
Xixo — 10:18
estás aí?
TiagoP — 10:46
Estou. Do que precisas?
Xixo
 iniciou uma chamada que durou 2 horas. — 10:47
Xixo — 11:31
{
  "blocked_domains": [
    "example-blocked.com",
    "another-blocked-site.org"
  ],
  "blocked_ips": [
Expandir
config(.json).txt
1 KB
# waf.py (Phase 3: Basic Pattern Matching)
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json # For loading the configuration file
import os   # For checking if config file exists
from urllib.parse import urlparse, parse_qs # For parsing URL paths and query strings

# --- Configuration Loading ---
CONFIG_FILE = 'config.json'
CONFIG = {}
LISTEN_PORT = 8080 # You can also move this to config.json if you like

def load_config():
    global CONFIG
    # Default configuration in case the file is missing or malformed
    default_config = {
        "blocked_domains": [],
        "blocked_ips": [],
        "blocked_paths_for_all_domains": [],
        "blocked_paths_for_specific_domain": {},
        "log_level": "INFO",
        "suspicious_query_patterns": [], # Added for Phase 3
        "blocked_user_agents": []      # Added for Phase 3
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
... (204 linhas)
Recolher
waf(.py).txt
16 KB
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
Imagem
﻿
Xixo
goat2889
 
# waf.py (Phase 3: Basic Pattern Matching)
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json # For loading the configuration file
import os   # For checking if config file exists
from urllib.parse import urlparse, parse_qs # For parsing URL paths and query strings

# --- Configuration Loading ---
CONFIG_FILE = 'config.json'
CONFIG = {}
LISTEN_PORT = 8080 # You can also move this to config.json if you like

def load_config():
    global CONFIG
    # Default configuration in case the file is missing or malformed
    default_config = {
        "blocked_domains": [],
        "blocked_ips": [],
        "blocked_paths_for_all_domains": [],
        "blocked_paths_for_specific_domain": {},
        "log_level": "INFO",
        "suspicious_query_patterns": [], # Added for Phase 3
        "blocked_user_agents": []      # Added for Phase 3
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
            # For this example, let's use exact match as per initial Phase 3 suggestion.
            if blocked_ua_pattern == user_agent: 
                self.send_block_response(f"User-Agent '{user_agent}' is blocked.")
                return
            # If you want partial match:
            # if blocked_ua_pattern.lower() in user_agent.lower():
            #     self.send_block_response(f"User-Agent containing '{blocked_ua_pattern}' is blocked (Full UA: '{user_agent}').")
            #     return

        # 6. Check Suspicious Query Parameter Patterns (Phase 3)
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
        # You can enable this if you want the default logging format,
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
waf(.py).txt
16 KB
