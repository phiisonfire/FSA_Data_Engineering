FROM apache/airflow:2.10.3

USER root

# Set working directory
WORKDIR /opt/airflow

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    libc6 \
    groff \
    less \
    && rm -rf /var/lib/apt/lists/*


# download the AWS CLI installer
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# unzip the installer
RUN unzip awscliv2.zip

# run the AWS CLI install script
RUN sudo ./aws/install

# clean up the installer files to reduce image size
RUN rm -rf awscliv2.zip aws

# verify installation
RUN aws --version

USER airflow

# copy .env file into the image
# this .env contains information about access key to aws iam user
COPY .env /etc/env/.env

# Export environment variables from the .env file
RUN set -a && \
    . /etc/env/.env && \
    set +a && \
    mkdir -p ~/.aws && \
    echo "[default]" > ~/.aws/credentials && \
    echo "aws_access_key_id=$AWS_ACCESS_KEY_ID" >> ~/.aws/credentials && \
    echo "aws_secret_access_key=$AWS_SECRET_ACCESS_KEY" >> ~/.aws/credentials && \
    echo "[default]" > ~/.aws/config && \
    echo "region=$AWS_DEFAULT_REGION" >> ~/.aws/config && \
    echo "output=$AWS_OUTPUT_FORMAT" >> ~/.aws/config

COPY requirements.txt .

RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r requirements.txt

USER root

RUN apt-get update && apt-get install -y openjdk-17-jdk && rm -rf /var/lib/apt/lists/*
RUN export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

USER airflow