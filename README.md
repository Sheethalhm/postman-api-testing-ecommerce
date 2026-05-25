🚀 AI-Augmented API Test Automation & Contract Testing Framework

⚡ Production-Style QA Engineering Project

An end-to-end API testing and validation framework that combines:

API test automation (Postman + Newman)
Contract testing (Schemathesis + OpenAPI 3.0)
CI/CD integration (GitHub Actions)
AI-powered failure analysis (Groq LLM)

👉 Built to simulate modern QA infrastructure used in microservice-based systems

🎯 Problem Statement

Modern APIs evolve quickly in distributed systems, leading to:

Broken API contracts between services
Slow debugging cycles for test failures
Lack of intelligent test failure insights
Manual validation in CI pipelines

💡 Solution
This project introduces a self-validating QA pipeline that:

✔ Automatically tests APIs
✔ Validates API contracts from OpenAPI
✔ Runs in CI/CD pipelines
✔ Uses AI to analyze failures and suggest fixes

🧠 Architecture Overview

Postman Collection
        ↓
Newman CLI Execution
        ↓
GitHub Actions CI Pipeline
        ↓
JUnit Test Report
        ↓
Schemathesis Contract Validation
        ↓
AI Failure Analyzer (Groq LLM)
        ↓
Root Cause + Fix Suggestions Report

🧰 Tech Stack
| Layer	            |    Tools            |
| API Testing       |	Postman           |
| Automation Runner |	Newman            |
| Contract Testing	|   Schemathesis      |
| API Spec	        |   OpenAPI 3.0       |
| CI/CD	            |  GitHub Actions     |
| AI Layer	        | Groq LLM (Llama 3)  |
| Scripting	        |  Python             |

⚙️ Key Features
🔹 API Test Automation
-- Functional + negative test coverage
-- Data-driven testing (CSV-based)
-- Environment-driven execution
-- Token extraction & reuse

🔹 Contract Testing (Schemathesis)
-- OpenAPI-based test generation
-- Schema validation & drift detection
-- Edge-case + fuzz testing
-- Early API break detection

🔹 CI/CD Pipeline Integration
-- Automated execution on push / PR
-- Newman CLI-based test runs
-- JUnit report generation
-- Ready for enterprise pipelines

🔹 AI-Powered Failure Analysis
-- Parses JUnit test failures
-- Detects root cause patterns:
	-- Auth failures
	-- Schema mismatches
	-- Status code deviations
-- Generates:
	-- Root cause explanation
	-- Fix recommendations
	-- Test improvement suggestions

🤖 AI Failure Analysis Example

❌ Raw Failure Output
401 Unauthorized
missing_api_key

✅ AI-Generated Insight
-- Root Cause: Missing authentication header (x-api-key)
-- Fix: Add API key to Postman environment variables
-- Recommendation: Add pre-request validation for auth headers

📊 Impact & Engineering Value

This project demonstrates:

-- Shift-left testing strategy
-- Contract-first API validation
-- CI/CD-ready QA automation
-- AI-assisted debugging workflows
-- Reduced manual test failure analysis time

📂 Project Structure
collections/        → Postman API collections
environments/       → Environment configs
data/               → Data-driven test inputs (CSV)
docs/               → Test strategy & documentation
newman/             → CLI execution scripts
reports/            → Test + AI analysis outputs
scripts/            → AI failure analyzers (Groq/Gemini)
openapi.yml         → API contract definition
.github/workflows/  → CI/CD pipeline

🚀 Getting Started
1️⃣ Clone Repository
git clone https://github.com/your-username/reqres-api-framework.git
cd reqres-api-framework

2️⃣ Run API Tests (Postman/Newman)
newman run collections/reqres_api_testing.postman_collection.json \
  -e environments/reqres-environment.postman_environment.json \
  -d data/users.csv

3️⃣ Run Contract Tests (Schemathesis)
schemathesis run openapi.yml --url https://reqres.in/api

4️⃣ Run AI Failure Analysis
python ai_failure_analyzer_groq.py reports/junit.xml

🧪 Testing Strategy
-- Functional API validation
-- Negative scenario coverage
-- Contract compliance testing
-- RFC compliance checks (e.g., 405/Allow header)
-- AI-based failure interpretation

📈 What This Project Demonstrates

This project reflects skills aligned with Senior QA / SDET / Platform QA roles:

-- API automation at scale
-- CI/CD integration mindset
-- Contract testing expertise
-- AI integration in engineering workflows
-- Debugging + observability thinking

🔮 Future Enhancements
-- AI-generated test case creation
-- Security testing integration (OWASP API)
-- Performance testing pipeline
-- Test observability dashboard
-- Kubernetes-based execution scaling

👤 Author

Sheethal Holenarasipura Maheswara
QA Automation Engineer | SDET | AI-in-Testing Enthusiast