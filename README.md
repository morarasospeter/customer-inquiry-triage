Customer Inquiry Triage System

This project is for the AI Software Developer Assessment - Caava VantagePoint AI.
It is a small system that classifies customer messages into categories like sales, billing, technical support, account management, or feedback.

Setup Instructions
1. Clone the repo
git clone <https://github.com/morarasospeter/customer-inquiry-triage.git>
cd <customer-inquiry-triage>

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate      # on Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the backend
uvicorn main:app --reload


This will start the backend at: http://127.0.0.1:8000/docs

5. Run the frontend
streamlit run app.py


This will open the frontend at: http://localhost:8501

Usage

Open the Streamlit frontend.

Type a customer message (example: "Please cancel my account").

The backend will return the category, reasoning, and confidence score.

Examples

"I can't log into my account" → TECHNICAL_SUPPORT

"Please cancel my account" → ACCOUNT_MANAGEMENT

"I need a demo before buying" → SALES

"My invoice has the wrong amount" → BILLING_INQUIRY

"I love your service!" → GENERAL_FEEDBACK

Design Choices and Trade-offs

I used a rule-based system with keywords because it is simple, fast, and does not depend on internet or external APIs.

Trade-off: it may miss cases where customers use unusual wording. A machine learning model would be more accurate.

Improvements with More Time

Use a pre-trained classifier (Hugging Face / OpenAI / Gemini) for better accuracy.

Make it provider agnostic (switch between AI providers easily).

Add scalability so new categories can be added by just updating a dictionary.

Suggest automatic responses from a small knowledge base.

Support PDFs or screenshots in addition to plain text.

Minimal Response

The API supports both full and minimal responses:

Full (default):

{
  "category": "TECHNICAL_SUPPORT",
  "reasoning": "Message mentions login problem",
  "score": 0.95
}


Minimal:

POST /triage?minimal=true


Response:

{ "category": "TECHNICAL_SUPPORT" }

Project Structure
project/
    main.py         # FastAPI backend
    app.py          # Streamlit frontend
    requirements.txt
    README.md
