FROM ubuntu:22.04

# Update the apt package list and install the necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    libsasl2-dev \
    libldap2-dev \
    default-libmysqlclient-dev \
    curl

# Optionally, clean up apt cache to reduce image size
RUN rm -rf /var/lib/apt/lists/*

# Install Apache Superset
RUN pip install apache-superset Pillow

# Copy the .env file from the host into the container
COPY .env /app/.env


# Export environment variables from the .env file
RUN set -a && \
    . /app/.env && \
    set +a

# Run Superset commands
RUN superset db upgrade && \
    superset fab create-admin && \
    superset init

# Expose the default port for Superset (8088)
EXPOSE 8088

# Set the default command to start the Superset server
CMD ["superset", "run", "-h", "0.0.0.0", "-p", "8088"]