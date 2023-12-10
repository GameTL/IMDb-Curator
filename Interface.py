# streamlit run '/Users/lilauto/Documents/GitHub/IMDb-Curator/src/Interface.py'

import streamlit as st
from model_inference import get_recommended_movies, dummy_json, get_movie_name_list


# Configure page to use wide mode
st.set_page_config(
    layout="wide", page_title="Movie Recommendations", page_icon=":clapper:"
)

# Presets
if "MovieList" not in st.session_state:
    st.session_state.MovieList = []
if "pressed" not in st.session_state:
    st.session_state.pressed = False


# Initialize the session state for the image if it doesn't exist
if "current_image" not in st.session_state:
    st.session_state.current_image = "img_database/1.jpg"  # default image


def get_movie_name_list_dummy():
    return (
        [
            "Avatar",
            "Pirates of the Caribbean: At World's End",
            "Spectre",
            "The Dark Knight Rises",
            "John Carter",
            "Spider-Man 3",
            "Tangled",
            "Avengers: Age of Ultron",
        ],
    )


# Function to simulate getting movie recommendations
def get_recommended_movies_dummy(movie_title):
    return [
        {
            "title": "Apollo 11",
            "genre": "Sci-Fi",
            "rating": "5.0",
            "synopsis": "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            "image": "apollo_18_poster.jpg",  # Replace with your actual image path or URL
        },
        {
            "title": "Apollo 18",
            "genre": "Sci-Fi",
            "rating": "5.0",
            "synopsis": "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            "image": "apollo_18_poster.jpg",  # Replace with your actual image path or URL
        },
        {
            "title": "Apollo 18",
            "genre": "Sci-Fi",
            "rating": "5.0",
            "synopsis": "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            "image": "apollo_18_poster.jpg",  # Replace with your actual image path or URL
        },
        {
            "title": "Apollo 18",
            "genre": "Sci-Fi",
            "rating": "5.0",
            "synopsis": "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            "image": "apollo_18_poster.jpg",  # Replace with your actual image path or URL
        },
        {
            "title": "Apollo 18",
            "genre": "Sci-Fi",
            "rating": "5.0",
            "synopsis": "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            "image": "apollo_18_poster.jpg",  # Replace with your actual image path or URL
        },
        {
            "title": "Apollo 18",
            "genre": "Sci-Fi",
            "rating": "5.0",
            "synopsis": "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            "image": "apollo_18_poster.jpg",  # Replace with your actual image path or URL
        },
    ]


# Function to display recommendations
def show_recommendations(recommended_movies):
    # Create columns for the movie posters
    cols = st.columns(len(recommended_movies))

    # Display movie posters side by side
    for col, movie in zip(cols, recommended_movies):
        with col:
            st.image(
                movie["Image Url (Title)"], width=150
            )  # Adjust the width as needed
            st.write(f"**{movie['Title']}**")
            st.write(f"Genre: {movie['genres']}")
            st.write(f"IMDB Rating: {movie['IMDB Rating']}")
            st.write(movie["Plot"])
            # st.markdown("---")  # Optional: visual separator


# Center the logo by using markdown with custom CSS

col1, col2 = st.columns([1, 1])
with col1:  # This is the center column
    st.image("logo.jpg", width=300)  # Adjust the width as needed
    st.markdown(
        """
        <h1 style=" color: white;">Movie Recommendations</h1>
    """,
        unsafe_allow_html=True,
    )
    # Add some space before the dropdown
    st.write("")


# Use a selectbox for the autocomplete dropdown styled with some padding
movie_title = st.selectbox(
    "Enter a movie title to get recommendations:",
    # get_movie_name_list_dummy(),
    get_movie_name_list(),
    index=0,
    format_func=lambda x: " " * 10 + x,  # Add padding to each option
)

# Add a styled recommend button
if st.button("🎬 Recommend"):
    if movie_title:
        # Get movie recommendations
        # st.session_state.MovieList = get_recommended_movies_dummy(movie_title)
        st.session_state.MovieList = get_recommended_movies(
            movie_name=movie_title, top_n=5
        )
        # st.session_state.MovieList = dummy_json

        # Check if the movie list is not empty
        if st.session_state.MovieList:
            # Set pressed to True to indicate recommendations are ready to display
            st.session_state.pressed = True

            # Display the first movie in col2
            if st.session_state.pressed:
                movie = st.session_state.MovieList[0]
                col2.image(
                    movie["Image Url (Title)"], width=150
                )  # Adjust the width as needed
                col2.write(f"**{movie['Title']}**")
                col2.write(f"Genre: {movie['genres']}")
                col2.write(f"IMDB Rating: {movie['IMDB Rating']}")
                col2.write(movie["Plot"])

            # Display remaining movies
            show_recommendations(st.session_state.MovieList[1:])
    else:
        st.error("Please enter a movie title to get recommendations.")
