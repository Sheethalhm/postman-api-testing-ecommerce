# ai_failure_analyzer.py

import json
import requests
import sys
import xml.etree.ElementTree as ET

def load_xml_report(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def extract_failures_from_xml(root):
    failures = []

    for testcase in root.iter("testcase"):
        for failure in testcase.findall("failure"):
            failures.append({
                "testcase": testcase.get("name"),
                "message": failure.text
            })

        for error in testcase.findall("error"):
            failures.append({
                "testcase": testcase.get("name"),
                "message": error.text
            })

    return failures


GEMINI_API_KEY = "AIzaSyCYj5pA9JwSYkhEhUhX_TjCiyLSwHccyNM"

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    f"models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
)

def call_gemini(failures):
    prompt = f"""
You are a Senior QA Engineer.

Analyze these API test failures:

{json.dumps(failures, indent=2)}

Provide:
- Root cause
- Fix
- Improvement suggestions
"""

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(GEMINI_URL, json=payload)
    return response.json()

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    root = load_xml_report("junit.xml")

    failures = extract_failures_from_xml(root)

    print(f"Failures found: {len(failures)}")

    result = call_gemini(failures)

    print(result)

