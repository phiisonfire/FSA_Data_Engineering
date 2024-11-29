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

# Export environment variables
RUN set -a && \
    . /app/superset/.env && \
    set +a

# Run Superset commands
RUN superset db upgrade && \
    superset fab create-admin --username $ADMIN_USERNAME --firstname Phi --lastname Nguyen --email $ADMIN_EMAIL --password $ADMIN_PASSWORD && \
    superset init

# Expose the default port for Superset
EXPOSE 8088

# Set the default command to start the Superset server
CMD ["superset", "run", "-h", "0.0.0.0", "-p", "8088"]
