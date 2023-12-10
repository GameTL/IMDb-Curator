# streamlit run '/Users/lilauto/Documents/GitHub/IMDb-Curator/src/Interface.py'

import streamlit as st

# Configure page to use wide mode
st.set_page_config(layout="wide", page_title="Movie Recommendations", page_icon=":clapper:")

# Function to simulate getting movie recommendations
def get_recommended_movies(movie_title):
    return [
         {
            'title': 'Apollo 18',
            'genre': 'Sci-Fi',
            'rating': '5.0',
            'synopsis': "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            'image': 'apollo_18_poster.jpg'  # Replace with your actual image path or URL
        },
        {
            'title': 'Apollo 18',
            'genre': 'Sci-Fi',
            'rating': '5.0',
            'synopsis': "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            'image': 'apollo_18_poster.jpg'  # Replace with your actual image path or URL
        },
        {
            'title': 'Apollo 18',
            'genre': 'Sci-Fi',
            'rating': '5.0',
            'synopsis': "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            'image': 'apollo_18_poster.jpg'  # Replace with your actual image path or URL
        },
        {
            'title': 'Apollo 18',
            'genre': 'Sci-Fi',
            'rating': '5.0',
            'synopsis': "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            'image': 'apollo_18_poster.jpg'  # Replace with your actual image path or URL
        },
        {
            'title': 'Apollo 18',
            'genre': 'Sci-Fi',
            'rating': '5.0',
            'synopsis': "A found footage film about a fictional mission to the moon that uncovers a deadly secret.",
            'image': 'apollo_18_poster.jpg'  # Replace with your actual image path or URL
        },
        
    ]

# Function to display recommendations
def show_recommendations(recommended_movies):
    # Create columns for the movie posters
    cols = st.columns(len(recommended_movies))
    
    # Display movie posters side by side
    for col, movie in zip(cols, recommended_movies):
        with col:
            st.image(movie['image'], width=150)  # Adjust the width as needed
            st.write(f"**{movie['title']}**")
            st.write(f"Genre: {movie['genre']}")
            st.write(f"Rating: {movie['rating']}")
            st.write(movie['synopsis'])
            st.markdown("---")  # Optional: visual separator

def main():
    # Center the logo by using markdown with custom CSS
    
    logo_path = 'logo.jpg'

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1,1,1,1,2,1,1,1,1])
    with col5:  # This is the center column
        st.image(logo_path, width=300)  # Adjust the width as needed


    st.markdown("""
        <h1 style="text-align: center; color: white;">Movie Recommendations</h1>
    """, unsafe_allow_html=True)
    # Add some space before the dropdown
    st.write("")

    # Use a selectbox for the autocomplete dropdown styled with some padding
    movie_title = st.selectbox(
        "Enter a movie title to get recommendations:",
        ["Avatar", "Pirates of the Caribbean: At World's End", "Spectre", "The Dark Knight Rises", "John Carter", "Spider-Man 3", "Tangled", "Avengers: Age of Ultron"],
        index=0,
        format_func=lambda x: ' ' * 10 + x  # Add padding to each option
    )

    # Add a styled recommend button
    if st.button("🎬 Recommend"):
        if movie_title:
            recommended_movies = get_recommended_movies(movie_title)
            show_recommendations(recommended_movies)
        else:
            st.error("Please enter a movie title to get recommendations.")

if __name__ == "__main__":
    main()
