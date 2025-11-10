import streamlit as st
import requests

st.set_page_config(page_title="Studio Ghibli API", page_icon="🎬")
st.title("🎬 Studio Ghibli Film Explorer")

st.write("Explore Studio Ghibli films using a real API! You can filter by director, sort, and view stats.")

url = "https://ghibliapi.vercel.app/films"
response = requests.get(url)
data = response.json()

directors = []
for movie in data:
    if movie["director"] not in directors:
        directors.append(movie["director"])
directors.sort()
directors.insert(0, "All Directors")

director_choice = st.selectbox("Choose a Director:", directors)
sort_choice = st.selectbox("Sort movies by:", ["release_date", "rt_score", "running_time"])
min_score = st.slider("Minimum Rotten Tomato Score:", 0, 100, 0)
show_scores = st.checkbox("Show Rotten Tomato Scores", value=True)

movie_list = []
for movie in data:
    if director_choice == "All Directors" or movie["director"] == director_choice:
        if movie["rt_score"].isdigit() and movie["running_time"].isdigit() and movie["release_date"].isdigit():
            if int(movie["rt_score"]) >= min_score:
                movie_list.append(movie)

def get_sort_value(movie):
    return int(movie[sort_choice])

movie_list.sort(key=get_sort_value)

st.subheader("🎥 Movie List")
for m in movie_list:
    st.write("**" + m["title"] + "** (" + m["release_date"] + ")")
    st.write("Director: " + m["director"] + " | Runtime: " + m["running_time"] + " min")
    if show_scores:
        st.write("Rotten Tomato Score: " + m["rt_score"])
    st.divider()

if len(movie_list) > 0:
    total_runtime = 0
    total_score = 0
    for m in movie_list:
        total_runtime += int(m["running_time"])
        total_score += int(m["rt_score"])

    avg_runtime = round(total_runtime / len(movie_list), 1)
    avg_score = round(total_score / len(movie_list), 1)

    st.subheader("📊 Summary Stats")
    st.write("Number of Movies:", len(movie_list))
    st.write("Average Runtime:", avg_runtime, "minutes")
    st.write("Average RT Score:", avg_score)

    runtimes = []
    scores = []
    for m in movie_list:
        runtimes.append(int(m["running_time"]))
        scores.append(int(m["rt_score"]))

    st.subheader("Runtime Chart")
    st.bar_chart(runtimes)

    if show_scores:
        st.subheader("RT Score Chart")
        st.line_chart(scores)

st.caption("Data source: Studio Ghibli API (https://ghibliapi.vercel.app/films)")
