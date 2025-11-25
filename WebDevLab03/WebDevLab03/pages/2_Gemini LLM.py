import streamlit as st
import google.generativeai as genai
import requests

genai.configure(api_key="AIzaSyDr6q9y767JfPG0Fg0BQm6kv96-5LitzcQ")

FILMS_URL = "https://ghibliapi.vercel.app/films"

def get_films():
    response = requests.get(FILMS_URL)
    response.raise_for_status()
    return response.json()

films = get_films()
film_titles = [f["title"] for f in films]

header = st.container()
selectors = st.container()
body = st.container()

with header:
    st.title("Studio Ghibli Gemini Comparison")
    st.write("Pick two Studio Ghibli films. Gemini will compare them and help a first-time viewer decide what to watch.")

with selectors:
    st.markdown("### Choose films to compare")
    col1, col2 = st.columns(2)
    with col1:
        filmA_title = st.selectbox("Film A", film_titles, index=0)
    with col2:
        filmB_title = st.selectbox("Film B", film_titles, index=1)

def find_film(title):
    for f in films:
        if f["title"] == title:
            return f
    return None

filmA = find_film(filmA_title)
filmB = find_film(filmB_title)

with body:
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Selected Films (API data)")
        st.json({"Film A": filmA, "Film B": filmB})

    with right_col:
        st.subheader("Gemini Response")
        if st.button("Ask Gemini"):
            if filmA_title == filmB_title:
                st.error("Please choose two different films.")
            else:
                prompt = f"""
You are a Studio Ghibli expert.

Using ONLY the JSON below, write a comparison that:
1. Summarizes each film.
2. Compares tone and themes.
3. Explains which film is better for a first-time viewer.
4. Ends with a recommendation sentence.

=== FILM A ===
{filmA}

=== FILM B ===
{filmB}
"""
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.write("Click **Ask Gemini** to generate a comparison.")
