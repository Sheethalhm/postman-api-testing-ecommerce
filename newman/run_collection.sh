#!/bin/bash

echo "Running Postman Collection..."

newman run ../collections/ecommerce.postman_collection.json \
-e ../environments/ecommerce_env.postman_environment.json \
-d ../data/users.csv \
--reporters cli,html \
--reporter-html-export report.html