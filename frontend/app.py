import streamlit as st
import requests

st.set_page_config(page_title="Customer Inquiry Triage", page_icon="🤖")

st.title("🤖 Customer Inquiry Triage")
st.write("Type a customer message below and see how it gets classified:")

message = st.text_area("Customer Message", height=150)

if st.button("Classify Message"):
    if message.strip():
        try:
            response = requests.post(
                "http://127.0.0.1:8000/triage",
                json={"message": message}
            )
            result = response.json()
            st.subheader("📌 Classification Result")
            st.json(result)
        except Exception as e:
            st.error("Error connecting to backend API. Make sure FastAPI server is running.")
    else:
        st.warning("Please enter a message before classifying.")
