# 🚀 E-Commerce API Testing using Postman

## 📌 Overview

This project demonstrates end-to-end API testing using Postman. It covers functional testing, negative testing, automation, and test data handling using a real-world e-commerce API.

## 🧰 Tools Used

* Postman
* Newman (CLI runner)
* FakeStore API

## 🌐 API Under Test

https://reqres.in/api

---

## 🎯 Key Features

* API request collections (Auth, Users, Products, Cart)
* Automated test scripts using JavaScript
* Environment variable management
* Data-driven testing using CSV
* Negative test scenarios
* CLI execution using Newman

---

## 📂 Project Structure

* `collections/` → Postman collection
* `environments/` → Environment variables
* `data/` → Test data
* `docs/` → Test documentation
* `newman/` → CLI execution scripts

---

## ⚙️ Setup Instructions

### 1. Import Collection

* Open Postman
* Import collection from `/collections`

### 2. Import Environment

* Import environment from `/environments`
* Select environment before running requests

---

## ▶️ Running Tests in Postman

* Open Collection Runner
* Select collection
* Choose environment
* Run all requests

---

## 🤖 Running via Newman

Install Newman:

```
npm install -g newman
```

Run collection:

```
newman run collections/ecommerce.postman_collection.json \
-e environments/ecommerce_env.postman_environment.json
```

---

## 🧪 Test Coverage

* Authentication validation
* User API testing
* Product API testing
* Cart workflow testing
* Negative scenarios

---

## 📊 Sample Assertions

* Status code validation
* Response time checks
* JSON structure validation
* Token extraction and reuse

---

## 📚 Learning Outcomes

* Understand API testing workflow
* Learn Postman scripting
* Implement real-world QA scenarios
* Practice automation using Newman

---

## 👩‍💻 Author

Sheethal Holenarasipura Maheswara

---
