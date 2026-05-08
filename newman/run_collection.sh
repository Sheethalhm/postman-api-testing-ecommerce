#!/bin/bash

echo "Running Postman Collection..."

newman run ../collections/reqres_api_testing.postman_collection.json \
-e ../environments/reqres-environment.postman_environment.json \
-d ../data/users.csv \
--reporters cli,html \
--reporter-html-export report.html