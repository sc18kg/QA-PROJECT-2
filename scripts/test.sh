#! /bin/bash

docker build -t testing-image -f testing/Dockerfile .
docker run -it -d --name testing-container testing-image

docker exec testing-container pytest ./frontend --cov ./frontend/application/
docker exec testing-container pytest ./app-2 --cov ./app-2/application/
docker exec testing-container pytest ./app-3 --cov ./app-3/application/
docker exec testing-container pytest ./app-4 --cov ./app-4/application/

docker stop testing-container
docker rm testing-container