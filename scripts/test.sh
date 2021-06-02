#! /bin/bash

docker build -t testing-image -f testing/Dockerfile .
docker run -it -d --name testing-container testing-image

docker exec testing-container pytest ./frontend --cov ./frontend/application/
docker exec testing-container pytest ./app2 --cov ./app2/application/
docker exec testing-container pytest ./app3 --cov ./app3/application/
docker exec testing-container pytest ./app4 --cov ./app4/application/

docker stop testing-container
docker rm testing-container