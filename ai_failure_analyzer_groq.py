import xml.etree.ElementTree as ET
from openai import OpenAI
from dotenv import load_dotenv
import json
import sys
import os

# =========================
# CONFIG
# =========================
load_dotenv()  # Load environment variables from .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.3-70b-versatile"

# =========================
# LOAD XML REPORT
# =========================

def load_xml_report(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

# =========================
# EXTRACT FAILURES
# =========================

def extract_failures(root):

    failures = []

    # Handle all testcases
    for testcase in root.iter("testcase"):

        testcase_name = testcase.get("name")

        # JUnit failure tag
        for failure in testcase.findall("failure"):

            failures.append({
                "testcase": testcase_name,
                "type": "failure",
                "message": failure.get("message"),
                "details": failure.text
            })

        # JUnit error tag
        for error in testcase.findall("error"):

            failures.append({
                "testcase": testcase_name,
                "type": "error",
                "message": error.get("message"),
                "details": error.text
            })

    return failures

# =========================
# AI ANALYSIS
# =========================

def analyze_failures(failures):

    if not failures:
        return "✅ No failures found in XML report."

    prompt = f"""
You are a Senior QA Automation Engineer.

Analyze these API test failures from a JUnit XML report.

Provide:
1. Root cause
2. Failure category
3. Fix recommendation
4. Additional test cases to add

Failures:
{json.dumps(failures, indent=2)}
"""

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": "You are an expert QA automation engineer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content or ""

# =========================
# MAIN
# =========================

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python ai_failure_analyzer_xml.py junit.xml")
        sys.exit(1)

    xml_file = sys.argv[1]

    print("📥 Loading XML report...")

    root = load_xml_report(xml_file)

    print("🔍 Extracting failures from XML...")

    failures = extract_failures(root)

    print(f"🚨 Failures found: {len(failures)}")

    print("\n🤖 Running AI analysis using Groq...\n")

    analysis = analyze_failures(failures)

    # =========================
    # SAVE REPORT
    # =========================

    output_file = "reports/AI_Failure_Analysis_Report.md"

    with open(output_file, "w", encoding="utf-8") as f:

        f.write("# AI Failure Analysis Report\n\n")

        f.write("## Summary\n")
        f.write(f"- Total Failures: {len(failures)}\n\n")

        f.write("## Failure Details\n\n")
        f.write("```json\n")
        f.write(json.dumps(failures, indent=2))
        f.write("\n```\n\n")

        f.write("## AI Analysis\n\n")
        f.write(analysis)

    print("===== AI FAILURE ANALYSIS =====\n")
    print(analysis)

    print(f"\n📄 Report saved to: {output_file}")