import streamlit as st

st.set_page_config(page_title="Lab03 Web App", page_icon="🌐", layout="wide")

st.title("🌐 CS 1301 – Web Development Lab 03")

st.subheader("Team Information")
st.write("**Section:** A3")
st.write("**Members:** Andrew Ko, Said Aslanov")

st.divider()

st.subheader("📋 About This App")
st.write("This multi-page web application was built using Streamlit for CS 1301 Lab 03.")

st.markdown("""
### 📑 Pages
1. **Studio Ghibli Film Explorer** – Uses a real API to show and analyze Studio Ghibli movie data.  
2. **LLM Analysis (Coming Soon)** – Will summarize Ghibli data using a Large Language Model (Part II).  
3. **Gemini Chatbot (Coming Soon)** – Will create a chatbot with knowledge about Studio Ghibli (Part II).  
""")

st.info("Use the sidebar to navigate between pages. Each page demonstrates a new part of the lab.")
