# Django, SQLite, Docker, Docker Compose
> This project uses a simple sqLite db for the demo purpose. <br>
**Borrowed Boilerplate codebase**: https://github.com/LondonAppDev/profiles-rest-api <br>
**YT Video Link**: [Dockerizing a Django REST Framework Project](https://www.youtube.com/watch?v=Y_rh-VeC_j4)

Docker has 2 stages: **build** & **run**. <br>
    **Build**: Docker looks for the Dockerfile, created an image & run all the commands declared in the DOckerfile. <br>
    **Run**: Runs a one-time command against a service.

## Procedure
**Dockerfile**
- Create a Dockerfile which will be used to copy the source code into the dcoker container.
- It'll also install the required python packages into the container's python environment.

**docker-compose.yml**
- Useful tool for docker containers while we want to cluster multiple different containers by setting dependecies between them.
- Create a single web service initially. 
- Its command will start the django server at 0.0.0.0:8080
    - [**Syntax**] `python project-root-dir/manage.py runserver 0.0.0.0:8080 `
    - [**Exact**]  `python src/profiles_project/manage.py runserver 0.0.0.0:8080`
- Its volume is mapped to the host machine's code within its docker file. So that, it'll automatically effect the mapping of that docker container if anything is modified in the source code. <br>
(*NB: It'll avoid the hassle of rebuilding & running the container each time we change something in the source code*)
- Port forwarding from the container to the local machine is defined as below.
    - [**Syntax**] hostPort:containerPort
    - [**Exact**]  `8001:8080`
- The migration is required in order to run the django project using a db. Thus, we need to override the command inside the docker-compose.yml file using the following command. <br>
    - **makemigrations**
        - [**Syntax**] `docker compose run serviceName python project-root-dir/manage.py makemigrations`
        - [**Syntax**] `docker compose run serviceName python src/profiles_project/manage.py makemigrations`
    - **migrate**
        - [**Syntax**] `docker compose run serviceName python project-root-dir/manage.py migrate`
        - [**Syntax**] `docker compose run serviceName python src/profiles_project/manage.py migrate`
- The `build` command will manually build the image without running the container. Whereas, the `up` with `-d` command will automatically build the image including starting up the container & service(s) within in the backgound.
    - `docker compose build`
    - `docker compose up -d`
- For creating a SUPERUSER using the command-line with manage.py script, use the following command.
    - `docker compose run web python src/profiles_project/manage.py createsuperuser`
- To shutdown the composed containers (services) use the floowing command.
    - `docker compose down`
