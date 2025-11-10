# Lab03 — Phase 1a & 1b Starter

## Run locally
```bash
pip install -r requirements.txt
streamlit run "Home_Page.py"
```

## Deploy on Streamlit Community Cloud (Phase 1b)
1. Create a **public GitHub repo** (e.g., `cs1301-lab03`).
2. Add/commit/push the entire `Lab03/` folder (keep `Home_Page.py` at the root of the repo or update the main file path during deploy).
3. Go to Streamlit Community Cloud and create a new app.
   - **Repository**: your repo
   - **Branch**: `main` (or your default)
   - **Main file path**: `Home_Page.py`
   - **Python version/requirements**: auto-detected from `requirements.txt`
4. Click **Deploy**. Your app URL will be generated.
5. Share the link and submit it with your zipped files per the assignment instructions.

> Keep using the `pages/` folder so links from the Home page continue to work after deployment.