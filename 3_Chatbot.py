import streamlit as st
import google.generativeai as genai
import requests

genai.configure(api_key="AIzaSyDr6q9y767JfPG0Fg0BQm6kv96-5LitzcQ")

MODEL_NAME = "gemini-2.0-flash"
FILMS_URL = "https://ghibliapi.vercel.app/films"

def get_films():
    response = requests.get(FILMS_URL)
    response.raise_for_status()
    return response.json()

films = get_films()
film_titles = [f["title"] for f in films]

st.title("Studio Ghibli Chatbot")

selected_titles = st.multiselect("Choose one or more films to chat about", film_titles, default=film_titles)

if "history" not in st.session_state:
    st.session_state.history = []

for speaker, text in st.session_state.history:
    if speaker == "user":
        st.markdown("**You:** " + text)
    else:
        st.markdown("**Bot:** " + text)

user_input = st.text_input("Ask a question about the selected films:", "")

if st.button("Send") and user_input.strip() != "":
    st.session_state.history.append(("user", user_input))

    if selected_titles:
        data_films = [f for f in films if f["title"] in selected_titles]
    else:
        data_films = films

    data_text = ""
    for f in data_films:
        data_text += (
            "Title: " + f["title"] + "\n"
            "Director: " + f["director"] + "\n"
            "Year: " + f["release_date"] + "\n"
            "Score: " + f["rt_score"] + "\n"
            "Description: " + f["description"] + "\n\n"
        )

    conversation_text = ""
    for speaker, text in st.session_state.history:
        conversation_text += speaker + ": " + text + "\n"

    prompt = (
        "You are a helpful Studio Ghibli chatbot.\n"
        "Use only the film data provided and give detailed responses. If the user asks about something not in the data, say you are not sure.\n\n"
        "Film data:\n" + data_text + "\n"
        "Conversation so far:\n" + conversation_text
    )

    model = genai.GenerativeModel(MODEL_NAME)

    try:
        response = model.generate_content(prompt)
        answer_text = response.text
    except Exception:
        answer_text = "Sorry, there was an issue connecting to the AI. Please try again."

    st.session_state.history.append(("bot", answer_text))
    st.rerun()
