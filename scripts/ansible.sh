#!/bin/bash

cd QA-PROJECT-2
git pull
git checkout ansible
ansible-playbook -i inventory playbook.yaml