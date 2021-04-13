##### *Start the postgres container*

`docker run -d \
    --name db \
    -e POSTGRES_PASSWORD=postgres \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /custom/mount:/var/lib/postgresql/data \
    postgres`

##### *create a new django project*
`docker-compose run web django-admin startproject book_store_proj .`

##### *Create a new django app*
`docker-compose run web python manage.py startapp book_store_app`

##### *Execute make makemigration command*
`docker-compose run web python manage.py makemigrations`

##### *Execute make migrate, so that the table gets created in the database*
`docker-compose run web python manage.py migrate`


##### *Create super user for django admin*
`docker-compose run web python manage.py createsuperuser`

 
##### *To access the database (get the container id using cmd - docker ps)*
`docker exec -it 728f78dc6a12 bash`

`psql -U postgres`

##### *build the docker compose file*
`docker-compose up --build`


##### *To start the project*
`docker-compose up`


##### *build docker image*
`sudo docker build -t django-postgres .`


##### *reference website*
https://docs.docker.com/compose/django/
