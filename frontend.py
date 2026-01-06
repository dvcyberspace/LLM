# frontend.py
import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:5000/audit")
HEALTH_URL = os.getenv("HEALTH_URL", "http://127.0.0.1:5000/health")

st.set_page_config(page_title="SOC Dashboard", page_icon="🛡️")

# UI Layout
st.title("🛡️ Security Operations Center")
st.markdown("### Automated Threat & Integrity Analysis")
st.divider()

# Sidebar for context
with st.sidebar:
    st.header("System Status")
    try:
        health = requests.get("http://127.0.0.1:5000/health")
        if health.status_code == 200:
            st.success("API Online")
        else:
            st.error("API Error")
    except:
        st.error("API Offline - Run api.py first!")
    
    st.info("Supported Tools:\n- Password Strength\n- SHA-256 Hashing\n- Security Advisory")

# Main Input Area
user_input = st.text_area("Enter Security Query:", 
                          placeholder="Example: Check the password strength of 'Admin123!' and give me its SHA-256 hash.")

if st.button("Run Security Audit", type="primary"):
    if user_input:
        with st.spinner("🤖 Agents are collaborating..."):
            try:
                # Send request to your Flask API
                payload = {"query": user_input}
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    result = data.get("result", "No result returned.")
                    
                    # Display Result
                    st.subheader("📝 Audit Report")
                    st.success(result)
                    
                    # Expandable details (optional debugging)
                    with st.expander("View Raw JSON Response"):
                        st.json(data)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the Backend API. Make sure `api.py` is running.")
    else:
        st.warning("Please enter a query first.")