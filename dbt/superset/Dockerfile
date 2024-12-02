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

# Export environment variables
# RUN set -a && \
#     . /app/superset/.env && \
#     set +a && \
#     superset db upgrade && \
#     superset fab create-admin --username $ADMIN_USERNAME --firstname Phi --lastname Nguyen --email $ADMIN_EMAIL --password $ADMIN_PASSWORD && \
#     superset init

# Run Superset commands
# RUN superset db upgrade
# RUN superset fab create-admin --username $ADMIN_USERNAME --firstname Phi --lastname Nguyen --email $ADMIN_EMAIL --password $ADMIN_PASSWORD
# RUN superset init

# Expose the default port for Superset
# EXPOSE 8088

# Set the default command to start the Superset server
# CMD ["superset", "run", "-h", "0.0.0.0", "-p", "8088"]

# Add the startup script
COPY docker-entrypoint.sh /app/superset/docker-entrypoint.sh
RUN chmod +x /app/superset/docker-entrypoint.sh

# Define environment variables
# ENV SECRET_KEY="HXdS8/Ny8qXgqKkG8IZkmgQL3wQT0D3M30n9RbHDOcC2iXGwLbBiWIpK"

ENTRYPOINT ["/app/superset/docker-entrypoint.sh"]
