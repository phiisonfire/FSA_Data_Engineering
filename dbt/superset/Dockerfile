FROM ubuntu:22.04

# Update apt repository and install dependencies in a single layer
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    python3.10 \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    libsasl2-dev \
    libldap2-dev \
    default-libmysqlclient-dev && \
    # Clean up apt cache to reduce image size
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN mkdir -p /app/superset
WORKDIR /app/superset

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the .env file from the host into the container
COPY .env /app/superset/.env

COPY superset_config.py .
ENV SUPERSET_CONFIG_PATH=/app/superset/superset_config.py

RUN apt-get update && apt-get -y install netcat

# Add the startup script
COPY docker-entrypoint.sh /app/superset/docker-entrypoint.sh
RUN chmod +x /app/superset/docker-entrypoint.sh

ENTRYPOINT ["/app/superset/docker-entrypoint.sh"]
