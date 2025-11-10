import streamlit as st

st.set_page_config(page_title="CS 1301 Lab03 Web App", page_icon="🌐", layout="wide")

# === EDIT THESE FIELDS ===
TEAM_NUMBER = "TBD"
SECTION = "TBD"
TEAM_MEMBERS = ["Your Name", "Teammate Name"]
# =========================

st.title("CS 1301 — Lab03: Streamlit Web App")
st.caption("Part I — Phase 1a (multi‑page setup) & Phase 1b (deployment‑ready)")

with st.container():
    st.subheader("Team Details")
    st.write(f"**Team Number:** {TEAM_NUMBER}")
    st.write(f"**Section:** {SECTION}")
    st.write("**Members:** " + ", ".join(TEAM_MEMBERS))

st.markdown("### What’s in this app?")
st.markdown(
    """
    1. **Home**: Overview & navigation.
    2. **API Analysis**: Analyze data from a web API (Phase 2).
    3. **LLM Processor**: Use Google Gemini to further process API data (Phase 3).
    4. **Chatbot**: A chatbot specialized on your API domain (Phase 4).
    """
)

st.divider()
st.markdown("#### Quick Navigation")
try:
    st.page_link("pages/1_API_Analysis.py", label="Open: Phase 2 — API Analysis")
    st.page_link("pages/2_Gemini_Processor.py", label="Open: Phase 3 — LLM Processor")
    st.page_link("pages/3_Chatbot.py", label="Open: Phase 4 — Chatbot")
except Exception:
    st.info("If links don’t appear, make sure this file is named `Home_Page.py` and other pages are inside a `pages/` folder.")

st.divider()
st.success("✅ Phase 1a complete when: Home loads, shows team info, and links open each sub‑page.")
st.info("Next: Deploy this repo to Streamlit Community Cloud for Phase 1b.")