## Requirements
Ensure you have a `.env` file in the same folder as your `Dockerfile`. Below is an example of the `.env` file:
```plaintext
AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
AWS_DEFAULT_REGION=ap-southeast-1
AWS_OUTPUT_FORMAT=json
AIRFLOW_UID=1000
AIRFLOW_GID=0
AIRFLOW_IMAGE_NAME=phinguyen/airflow:latest
```

## Build image from Dockerfile
Ensure the current working directory is where Dockerfile located
```bash
docker build -t phinguyen/airflow:latest .
```

## Key takeaway from Dockerfile
### Commands:
- `FROM`: define base image
    - Base image apache/airflow:2.10.3 have a user `airflow`
- `USER`: change user
- `WORKDIR`: choose working directory
- `RUN`: for running bash commands
    - `&&`: for running multiple bash commands in 1 RUN instruction
- `COPY`: copy files from local into image

## Key takeaway from docker-compose.yml
1. Anchors `&` and Reference `<<: *`
    - Anchors `&` assigns a specific section of YAML content to a variable, exp `&airflow-common`
    - Reference reuse that specific section by using `<<: *airflow-common`
    - Detail example:
```yaml
x-airflow-common:
  &airflow-common # this anchor contains the content of all elements below it including image, environment, volumes, user, depends_on
  image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.10.3}
  environment:
    &airflow-common-env
    AIRFLOW__CORE__EXECUTOR: CeleryExecutor
    ...
  volumes:
    - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
    ...
  user: "${AIRFLOW_UID:-50000}:0"
  depends_on:
    &airflow-common-depends-on
    redis:
      condition: service_healthy

services:
  airflow-webserver:
    <<: *airflow-common # reference to the anchor above
    command: webserver
    ports:
      - "8080:8080"
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully
```

2. Syntax `${AIRFLOW_IMAGE_NAME:-apache/airflow:2.10.3}`
Define the default value `apache/airflow:2.10.3` if environment variable `AIRFLOW_IMAGE_NAME` is not set.

3. Dive deep into docker-compose service's components
- `environment`: define environment variables for container
- `volumes`: mount files, folders in local into container
- `user`: define the user under which the container should run, this helps control permissions of files and processes within the container
- `depends_on`: ensure services defined here is healthy before start the container
- `expose`: declare which ports that container should expose to other containers within the same Docker network
- `healthcheck`: 
  - define a command that Docker periodically run to check if the container is healthy
  - Docker can restart the container (based on restart policy)
- `ports`: map container ports to the host machine
  - `- "host_port: container_port"`
- `command`: specify the command to run when the container starts, override the default `CMD` instruction in the Docker image

entrypoint vs CMD
- CMD giup ta truyen arguments
- entrypoint thi ta ko the overwrite





