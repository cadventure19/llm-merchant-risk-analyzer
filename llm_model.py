import json
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()  # loads variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_summary(merchant_json):
    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
    You are a senior fraud and risk analyst at a fintech company.
    You are given detailed data about a merchant including:
    - Transaction-level data (flows, categories, and statuses)
    - Aggregated metrics (volume, success rates, ATS, 7d/30d/90d comparisons)
    - Merchant profile and behavioral data (classification, suspicious flags, rule blocks)

    Your task is to produce a structured and detailed RISK SUMMARY of this merchant.

    Please provide the output in the following structured format:

    **1. Overall Risk Assessment**
       - Level (Low / Medium / High)
       - Brief justification (1–2 lines on top contributing signals)

    **2. Transactional Behavior Analysis**
       - Key patterns in transaction volume, amount, and flow sources
       - Anomalies (sudden spikes, external inflows, failed txns, or repeated senders)
       - Behavioral shifts over 7d/30d/90d

    **3. Merchant Profile Insights**
       - Risk model or AML classification (if available)
       - Suspicious activity indicators (chargebacks, blocked rules, etc.)
       - Behavior consistency with low-risk merchants

    **4. Key Risk Drivers**
       - List 3–5 major drivers or metrics indicating elevated or reduced risk.
       - Example: High refund ratio, high ATS volatility, multiple inflow accounts, poor success rate.

    **5. Recommendation / Next Actions**
       - Suggest 2–3 risk control actions (e.g., monitoring, hold review, UPI inflow checks)
       - Keep them practical and data-driven.

    Here is the merchant data:
    {merchant_json}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


# ---- Load merchant_json.json automatically ----
if __name__ == "__main__":
    with open("merchant_json.json", "r") as f:
        merchant_data = json.load(f)  # Load JSON as a Python dict

    # Convert dict to a formatted string
    merchant_json_str = json.dumps(merchant_data, indent=2)

    summary = generate_summary(merchant_json_str)
    print(summary)