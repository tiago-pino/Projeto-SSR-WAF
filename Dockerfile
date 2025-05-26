# Dockerfile

# 1. Start with an official Python base image.
FROM python:3.9-bookworm
ENV PYTHONUNBUFFERED=1

# Define arguments for the keyring package URL and filename
# Updated to the version found in the Debian pool: 2023.3+deb12u2
ARG DEBIAN_KEYRING_PKG_FILENAME=debian-archive-keyring_2023.3+deb12u2_all.deb
ARG DEBIAN_KEYRING_PKG_URL=http://ftp.debian.org/debian/pool/main/d/debian-archive-keyring/${DEBIAN_KEYRING_PKG_FILENAME}

# Use Docker's ADD instruction to download the keyring package directly into the image.
ADD ${DEBIAN_KEYRING_PKG_URL} /tmp/${DEBIAN_KEYRING_PKG_FILENAME}

# Install the downloaded keyring package FIRST.
RUN echo "Attempting to install debian-archive-keyring with dpkg..." && \
    dpkg -i /tmp/${DEBIAN_KEYRING_PKG_FILENAME} && \
    rm /tmp/${DEBIAN_KEYRING_PKG_FILENAME} && \
    echo "debian-archive-keyring installation via dpkg attempted."

# Now that the keyring is (hopefully) installed, update apt and install your tools.
RUN echo "Attempting apt-get update and package installation..." && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        iputils-ping \
        dnsutils \
        gnupg \
    && rm -rf /var/lib/apt/lists/* && \
    echo "apt-get update and package installation successful."

# 2. Set the working directory inside the container.
WORKDIR /app

# 3. Copy the requirements file into the container.
COPY requirements.txt .

# Update pip first
RUN pip install --no-cache-dir --progress-bar off --upgrade pip

# 4. Install the Python dependencies listed in requirements.txt.
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

# 5. Copy your WAF Python script into the container.
COPY waf.py .

# 6. Tell Docker that your application will listen on port 8080 inside the container.
EXPOSE 8080

# 7. Define the command to run when the container starts.
CMD ["python", "waf.py"]
