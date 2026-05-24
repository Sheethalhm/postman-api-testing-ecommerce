# 🚀 ReqRes API Testing using Postman

## 📌 Overview

This project demonstrates end-to-end API testing using Postman. It covers functional testing, negative testing, automation, and test data handling using the ReqRes API.

## 🧰 Tools Used

* Postman
* Newman (CLI runner)

## 🌐 API Under Test

https://reqres.in/api

---

## 🎯 Key Features

* API request collections (Users, Auth)
* Automated test scripts using JavaScript
* Environment variable management
* Data-driven testing using CSV (`data/users.csv`)
* Negative test scenarios
* CLI execution using Newman

---

## 📂 Project Structure

* `collections/` → Postman collection (`reqres_api_testing.postman_collection.json`)
* `environments/` → Environment variables (`reqres-environment.postman_environment.json`)
* `data/` → Test data (`users.csv`)
* `docs/` → Test documentation (`learning-guide.md`, `test-scenarios.md`, `test-strategy.md`)
* `newman/` → CLI execution scripts (`run_collection.sh`)

---

## ⚙️ Setup Instructions

### 1. Import Collection

* Open Postman
* Import collection from `collections/reqres_api_testing.postman_collection.json`

### 2. Import Environment

* Import environment from `environments/reqres-environment.postman_environment.json`
* Select environment before running requests

---

## ▶️ Running Tests in Postman

* Open Collection Runner
* Select `ReqRes API Testing` collection
* Choose `reqres-environment` environment
* (Optional) Add data file `data/users.csv` for data-driven tests
* Run all requests

---

## 🤖 Running via Newman

Install Newman:

```
npm install -g newman
```

Run collection with environment and data file:

```
newman run collections/reqres_api_testing.postman_collection.json \
	-e environments/reqres-environment.postman_environment.json \
	-d data/users.csv
```

Or use the provided shell script (Linux/Mac):

```
cd newman
sh run_collection.sh
```

---

## 🧪 Test Coverage

* Authentication validation
* User API testing
* Negative scenarios
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
* Use data-driven testing with CSV
* Integrate API tests with CI/CD (see `.github/workflows/` if available)
---

## 📝 Documentation

See the `docs/` folder for:
- `learning-guide.md`: Postman and API testing basics
- `test-scenarios.md`: List of test scenarios
- `test-strategy.md`: Test approach and strategy

---

## 💡 Improvements & Contribution

- Add more negative and edge case scenarios
- Integrate with CI/CD for automated runs
- Add badges for build/test status
- Add a License section if open-sourcing
- Contributions welcome! Open issues or submit PRs

---

## 👩‍💻 Author

Sheethal Holenarasipura Maheswara

---
