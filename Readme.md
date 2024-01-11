# CRUD application using FastAPI

This project is a sample CRUD application that utilises FastAPI to make REST API calls to a RDBMS like postgresql.

## Description

This project aims at making CRUD operations possible over an web application. In this project there are methods that helps in management of users and the products that they buy. We can create any user, read all the details of a uer, update his/her name and can even delete a user entry in case of user management. We can create an item entry that a user bought, list the items that are bought by a user, update the  product bought by an user and can delete the item entry entered by mistake in case of item management. These operations are made possible by using the FastAPI and connecting it with a RDBMS. This API can be tested using SwaggerUI provided by FastAPI without using any frontend page.

## Getting Started

### Dependencies

* Any OS is supported for this project
* python>=3.10
* fastapi>=0.68.0,<0.69.0
* pydantic>=1.8.0,<2.0.0
* uvicorn>=0.15.0,<0.16.0
* greenlet==3.0.3
* sqlalchemy==2.0.25
* psycopg2-binary==2.9.9

### Installing

* git clone https://github.com/guhan-mps/CRUD/tree/master
* If you are going to execute directly on your system set the **DatabaseURL** environment variable to your postgresql connection string in the format postgresql://\[USER\]:\[PASSWORD\]@localhost/\[DATABASE\], **UserModelName** environment variable as your user table name and **ItemModelName** environment variable as your items table name
* If you are deploying on docker compose, change the **DatabaseURL** environment variable in the docker-compose.yml under python service in the format postgresql://\[USER\]:\[PASSWORD\]@pgsql/\[DATABASE\], **UserModelName** environment variable as your user table name and **ItemModelName** environment variable as your items table name. Also change the environment variables under pgsql service according to the **DatabaseURL** provided.
* If you are deploying on kubernetes, we would need to hash the environment variable contents into base64 format
    - For Windows: powershell \"\[convert\]::ToBase64String\(\[Text.Encoding\]::UTF8.GetBytes\(\"\[CONTENT\]\"\)\)\"
    - For Ubuntu: echo -n \"\[CONTENT\]\" | base64
    - Set the base64 encoded value of postgresql user, password and database in postgres-username, postgres-password, postgres-database fields of postgres-secret.yaml
    - Set the base64 encoded value of Database connection string, users table name and items table name in DatabaseURL, UserModelName and ItemModelName fields of fastapi-secret.yaml

### Executing program
* Stay on the CRUD directory
* For **Execution on the System** 
```
uvicorn backendapi.sql_app.main:app --reload --host 0.0.0.0 --port 8000
```
Now the API runs and can be accessed using SwaggerUI using <http://0.0.0.0:8000/docs>
* For **Docker compose deployment**
```
docker compose up --build
```
Now the API runs and can be accessed using SwaggerUI using <http://0.0.0.0:8000/docs>

* For **Kubernetes deployment on minikube cluster** navigate to deployment directory and run:
```
minikube start
kubectl apply -f pv.yaml
kubectl apply -f pvc-dynamic.yaml
kubectl apply -f postgres-secret.yaml
kubectl apply -f postgres-statefulset.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f fastapi-secret.yaml
kubectl apply -f fastapi-deployment.yaml
kubectl apply -f fastapi-service.yaml
```
Now the API could be accessed via SwaggerUI in the url <http://$(minikube ip):30008/docs>
