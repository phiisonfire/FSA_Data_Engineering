# Question 1: Online Extraction vs Offline Extraction

## Online Extraction
- Occurs in **real-time** or **near real-time**
- Pulls data from the source system when new data arrive
- Used in scenarios when timely data is critical

## Offline Extraction
- Offline extraction retrieves data in **batch** mode, typically at scheduled intervals (e.g., hourly, nightly). 
- The data is often read from a snapshot or a backup of the source system, minimizing the impact on live operations.

# Question 2: ETL vs ELT
## ETL
- Data is extracted from the source, transformed into the desired format, and then loaded into the destination system.
- 

# Question 4: Why docker-compose?

References:
- https://docs.docker.com/compose/intro/features-uses/
- https://docs.docker.com/compose/how-tos/production/

## Key benefits
- Simplified control:
    - allow us to define & manage multiple-container applications in a single `YAML` file.
    - simplify the complex task of orchestrating & coordinating various services
- Efficient collaboration:
    - docker-compose.yml files are easy to share among teams
- Portability across environments:
    - `Compose` supports variables -> customize the composition for different environments

## Common use cases

### Development environments
- helps developers quickly create an isolated environment for developing application

### Automated testing environments
- Automated end-to-end testing requires an environment in which to run tests.

### Compose in production
- The easiest way to deploy an application is to run it on a single server, 
similar to how you would run your development environment. 
- If you want to scale up your application, you can run Compose apps on a Swarm cluster.
- Modify your Compose file for production
    - Removing any volume bindings for application code, so that code stays inside the container and can't be changed from outside
    - Binding to different ports on the host
    - Setting environment variables differently, such as reducing the verbosity of logging, or to specify settings for external services such as an email server
    - Specifying a restart policy like restart: alwaysto avoid downtime
    - Adding extra services such as a log aggregator



