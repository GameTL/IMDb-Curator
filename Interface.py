# streamlit run '/Users/lilauto/Documents/GitHub/IMDb-Curator/src/Interface.py'

import streamlit as st
from model_inference import get_recommended_movies, dummy_json, get_movie_name_list, get_movie_name_list_dummy


# dummy = True
dummy = False

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





# Function to display recommendations
def show_recommendations(recommended_movies, rating_range):
    st.markdown("---")  # Optional: visual separator
    st.markdown(
        f"""
        <h2 style=" color: white;">Because you watch {movie_title}</h1>
    """,
        unsafe_allow_html=True,
    )
    # Add vertical space
    st.markdown("###")  # This adds a bit of space using markdown

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


if dummy:
    # Use a selectbox for the autocomplete dropdown styled with some padding
    movie_title = st.selectbox(
        "Enter a movie title to get recommendations:",
        get_movie_name_list_dummy(),
        index=0,
        format_func=lambda x: " " * 10 + x,  # Add padding to each option
    )
else:
    # Use a selectbox for the autocomplete dropdown styled with some padding
    movie_title = st.selectbox(
        "Enter a movie title to get recommendations:",
        get_movie_name_list(),
        index=0,
        format_func=lambda x: " " * 10 + x,  # Add padding to each option
    )

bncol1, bncol2, bncol3 = st.columns([1, 1,1])

with bncol2:
    num_recommendation = st.slider(label='Number of Recommendations',min_value=1, max_value=10, value=5,step=1)
with bncol3:
    rating_range = st.slider(label='IMBd Rating',min_value=0.0, max_value=10.0, value=(5.0, 10.0),step=0.1) # (1.6, 10.0)
    # st.write('Values:', values)

with bncol1:

    # Add a styled recommend button
    if st.button("🎬 Recommend",use_container_width=True ):
        if movie_title:
            # Get movie recommendations
            # st.session_state.MovieList = get_recommended_movies_dummy(movie_title)
            if dummy:
                st.session_state.MovieList = dummy_json[:num_recommendation +1]
            else:
                st.session_state.MovieList = get_recommended_movies(
                    movie_name=movie_title, top_n=num_recommendation, rating_range=rating_range
                )


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
        else:
            st.error("Please enter a movie title to get recommendations.")

# Display the first movie and remaining recommendations in bncol2 if pressed
if st.session_state.pressed and st.session_state.MovieList:
    # Display remaining movies
    show_recommendations(st.session_state.MovieList[1:], rating_range)
