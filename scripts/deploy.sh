#! /bin/bash

ssh Kieron@35.189.91.113 << EOF
cd QA-PROJECT-2
git pull
env DATABASE_URI=${DATABASE_URI} env SECRET_KEY=${SECRET_KEY} env MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} docker stack deploy --compose-file docker-compose.yaml qa-project-2_stack
EOF