# Merchant Risk Analyzer with LLM

Generate structured merchant risk summaries using a Large Language Model (LLM) on transaction, profile, and behavioral data.

This project leverages OpenAI’s LLM (`gpt-4o-mini`) to analyze merchant data, detect potential risks, and produce actionable recommendations in a structured format.

## Features

- Analyzes **transaction-level data** (flows, categories, amounts, statuses)
- Processes **aggregated metrics** (success rates, average transaction size, 7d/30d/90d comparisons)
- Evaluates **merchant profile and behavioral indicators** (classification, suspicious flags, rule blocks)
- Generates a **structured risk summary** with:
  1. Overall Risk Assessment
  2. Transactional Behavior Analysis
  3. Merchant Profile Insights
  4. Key Risk Drivers
  5. Recommendations / Next Actions

## Repository Structure

├─ llm_model.py # Main code for merchant risk analysis
├─ merchant_json.json # Sample merchant data
├─ requirements.txt # Python dependencies




## Installation

1. Clone the repository:

```bash
git clone  https://github.com/cadventure19/llm-merchant-risk-analyzer.git
cd llm-merchant-risk-analyzer

```

2. (Optional but recommended) Create a virtual environment:

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install dependencies:

```
pip install -r requirements.txt
```


Setup

Create a .env file in the root folder with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

Important: Do not commit .env to GitHub to keep your API key secure.


Usage

Run the main script to generate a merchant risk summary:


python llm_model.py


The script will read merchant_json.json, analyze the data using the LLM, and print a structured risk summary to the console.


Notes

This project does not store or share sensitive merchant data; only the LLM processes it temporarily in memory.

Adjust the temperature in llm_model.py to control response creativity (default is 0.3 for focused, deterministic summaries).


