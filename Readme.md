Database runs in the namespace of the container. So the Database URL must contain the container name instead of localhost.

Do not use port 5432 explicitly in yaml of postgres

Hashed contents in Linux
echo -n "content" | base64

Hashed contents in Windows
powershell "[convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes(\"postgresql://postgres:admin@localhost:5432/db\"))"

SSH into minikube
ssh -i ~/.minikube/machines/minikube/id_rsa docker@$(minikube ip)

Accessing any running container(also within minikube)
docker exec -it CONTAINER_NAME bash

Execution:
    -Normal execution: uvicorn backendapi.sql_app.main:app --reload
    -Docker compose: docker compose up --build
    -Kubernetes: kubectl apply -f [yaml file](Executed in the order Secrect -> Deployment -> Service)