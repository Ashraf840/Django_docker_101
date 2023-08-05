# Django, Postgresql, Docker, Docker Compose
> This project uses a simple sqLite db for the demo purpose. <br>
**Borrowed Boilerplate codebase**: https://github.com/LondonAppDev/profiles-rest-api <br>
**YT Video Link**: [Setting up PostgreSQL database with a Django Docker application
](https://www.youtube.com/watch?v=610jg8bK0I8)

Docker has 2 stages: **build** & **run**. <br>
    **Build**: Docker looks for the Dockerfile, created an image & run all the commands declared in the DOckerfile. <br>
    **Run**: Runs a one-time command against a service.

## Procedure
**Dockerfile**
- Create a Dockerfile which will be used to copy the source code into the dcoker container.
- It'll also install the required python packages into the container's python environment. <br>

**docker-compose.yml**
- Modify the exisiting docker-compose.yml file to add postgres-db as a new srevice. (NB: This new db-service will be connected to the web-service)
- Unlike the web-service which build image from the current directory, the docker-compose will look for the latest postgres-db-image from the internet.
    - `image: postgres:latest`
- Before the web-service is ever to run, the db-service is required to perform first. Thus, we need to declare a new item `depends_on` in the web-service.
    - `depends_on: - db` <br>
    (*NB: This `db` is the db-service-name defined in the docker-compose.yml file.*)
- Install '**psycopg2-binary**' python-libray in order to work with postgresql.
- Change the DATABASE configuration in the src/profiles_project/profiles_project/settings.py file in accordance with the db-credentials (*will be defined*) in the db-service.
- Add volumes to this db-service (**./pgdata/**). Thus it'll make the project's db-volume consistent regardless of the docker containers.
- Port forwarding (*db-service*) from the container to the local machine is defined as below.
    - [**Syntax**] hostPort:containerPort
    - [**Exact**]  `8002:5432` 
- Define the environment-variables of db-service which will be used as credentials of web-service in order to properly functioning.
- Define new image name for both the web & db services.
    - [web] `image: docker-compose-102:latest`
    - [db] `image: postgres:latest`
- Define new container names for both the services.
    - [web] `container_name: docker-compose-102-codebase-container`
    - [db] `container_name: docker-compose-102-db-container`
- It's required to perform the migrations to the postgres-db-service uisng the following command. (*NB: Change to root-user before performing the migration operation*)
    - [migrations] `docker compose run web python src/profiles_project/manage.py makemigrations`
    - [migrate] `docker compose run web python src/profiles_project/manage.py migrate`
- The `build` command will manually build the image without running the container. Whereas, the `up` with `-d` command will automatically build the image including starting up the container & service(s) within in the backgound.
    - `docker compose build`
    - `docker compose up -d`
- For creating a SUPERUSER using the command-line with manage.py script, use the following command.
    - `docker compose run web python src/profiles_project/manage.py createsuperuser`
- To shutdown the composed containers (services) use the floowing command.
    - `docker compose down`
