import os
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import json
import numpy as np


dummy_json = [
    {
        "Unnamed: 0": 405,
        "Best Picture": "None",
        "Certificate (GB)": "12",
        "Certificate (US)": "PG-13",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        "Plot": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
        "Production Companies (1st)": "Marvel Studios",
        "Title": "The Avengers",
        "Title Id": "tt0848228",
        "Year of Release": 2012,
        "IMDB Rating": 8.0,
        "Runtime (Minutes)": 143.0,
        "Lead Actors": "['Jamie McShane', 'Chris Hemsworth', 'Clark Gregg', 'Walter Perez', 'Donald Li', 'Tom Hiddleston', 'Daniel Crowder', 'John Wood', 'David Webber', 'Alexis Denisof', 'Warren Kole', 'Jesse Garcia', 'Arthur Darbinyan', 'Eddie Izzard', 'Cobie Smulders', 'Ashley Johnson', 'Joss Whedon', 'Nicholas Woodeson', 'Dieter Riesle', 'Enver Gjokaj', 'Josh Cowdery', 'Brent McGee', 'Michael Zhang', 'Rashmi Rustagi', 'Alicia Sixtos', 'Andrea Vecchio', 'Kelley Robins Hicks', 'Fernanda Toker', 'Keeley Hawes', 'Kirill Nikiforov', 'Maximiliano Hern\u00e1ndez', 'Richard Lumsden', 'Jerzy Skolimowski', 'Yumiko Komatsu', \"M'laah Kaur Singh\", 'Momoko Komatsu', 'Robin Swoboda', 'Robert Downey Jr.', 'Samuel L. Jackson', 'Kenneth Tigar', 'Fiona Shaw', 'Katsumi Komatsu', 'Ralph Fiennes', 'Sean Connery', 'Jeff Wolfe', 'Powers Boothe', 'Paul Bettany', 'Patrick Macnee', 'Jim Broadbent', 'Stellan Skarsg\u00e5rd', 'Harry Dean Stanton', 'Robert Clohessy', 'Gwyneth Paltrow', 'Jenny Agutter', 'Uma Thurman', 'Nadim Sawalha', 'Mark Ruffalo', 'Jeremy Renner', 'Shaun Ryder', 'Scarlett Johansson', 'William Christopher Stephens', 'Chris Evans', 'James Eckhouse', 'Tina Benko', 'Michael Godley', 'Christopher Godwin', 'Romy Rosemont', 'Eileen Atkins', 'Jeremiah S. Chechik', 'Carmen Ejogo']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['stop', 'team', 'fight']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 509,
        "Best Picture": "None",
        "Certificate (GB)": "18",
        "Certificate (US)": "R",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BNWI0NTc4YWYtZDYzYy00NGUyLWI0ODMtMGIxOWQxY2RlZDQ5XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg",
        "Plot": "The \"universal soldiers\" must fight the whole army, when the military's supercomputer S.E.T.H gets out of control.",
        "Production Companies (1st)": "TriStar Pictures",
        "Title": "Universal Soldier: The Return",
        "Title Id": "tt0176269",
        "Year of Release": 1999,
        "IMDB Rating": 4.2,
        "Runtime (Minutes)": 83.0,
        "Lead Actors": "['Michael Jai White', 'Daniel von Bargen', 'Brent Hinkley', 'Dion Culberson', 'Barbara Petricini-Buxton', 'Jacqueline Klein', 'Sam Williamson', 'Justin Lazard', 'Woody Watson', 'James Black', 'Jean-Claude Van Damme', 'Heidi Schanz', 'Bill Goldberg', 'Brent Anderson', 'Josh Berry', 'Kiana Tom', 'Mark Duke Dalton', 'Xander Berkeley', 'Molly Moroney', 'Karis Paige Bryant', 'Maria Arita', 'Mic Rodgers', 'Pam Dougherty', 'Heidi Franz']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['gets', 'fight']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 3515,
        "Best Picture": "None",
        "Certificate (GB)": "18",
        "Certificate (US)": "R",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BZGE3ODg2YmYtMzdhYy00MzdhLWIyZTctM2IxNDNmNmYyNmRlXkEyXkFqcGdeQXVyMTQ3Njg3MQ@@._V1_.jpg",
        "Plot": "After a devastating nuclear war, the last fertile woman on Earth joins forces with a tough renegade warrior to fight a team of deadly cyborgs and save the human race from extinction.",
        "Production Companies (1st)": "Global Pictures",
        "Title": "American Cyborg: Steel Warrior",
        "Title Id": "tt0109098",
        "Year of Release": 1993,
        "IMDB Rating": 4.3,
        "Runtime (Minutes)": 94.0,
        "Lead Actors": "['Jack Widerker', 'David Milton-Jones', 'Alon Nashman', 'Joe Lara', 'Helen Lesnick', 'Joe Kaplan', 'Eric Storch', 'John Saint Ryan', 'Andrea Litt', 'Nicole Hansen', 'Jack Adalist', 'Uri Gavriel', 'Nicole Berger', 'Yosef Shiloach', 'Kevin Patterson', 'P.C. Frieberg', 'Boaz Davidson']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['save', 'war', 'woman', 'team', 'fight']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 758,
        "Best Picture": "None",
        "Certificate (GB)": "15",
        "Certificate (US)": "PG-13",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BZTlhNzgxYTEtZmNjMi00NTI5LWE1ODUtYTlmMjZlNzc4MjI5XkEyXkFqcGdeQXVyMTUzMDUzNTI3._V1_.jpg",
        "Plot": "A gruff bounty hunter travels back in time to 1980s Los Angeles to stop a twisted criminal who can transform people into zombie-like creatures.",
        "Production Companies (1st)": "Empire Pictures",
        "Title": "Trancers",
        "Title Id": "tt0090192",
        "Year of Release": 1984,
        "IMDB Rating": 6.0,
        "Runtime (Minutes)": 76.0,
        "Lead Actors": "['Biff Manard', 'Brad Logan', 'Art LaFleur', 'Ed McClarty', 'Barbara Perry', 'Anne Seymour', 'Lantza Krantz', 'Don Ross', 'Michael McGrady', 'Michael Heldebrant', 'Minnie Summers Lindsey', 'Alyson Croft', 'Tony Malone', 'Richard Herd', 'Wiley Harker', 'Steve Jensen', 'Helen Hunt', 'Tim Thomerson', 'Michael Stefani', 'Pete Schrum', 'Nickey Beat', 'Richard Erdman', 'Telma Hopkins', 'Kymberly Sheppard', 'Charles Band', 'Miguel Fernandes']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['stop', 'people', 'time']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 755,
        "Best Picture": "None",
        "Certificate (GB)": "12",
        "Certificate (US)": "Not Rated",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BMzQwZDg1MGEtN2E5My00ZDJlLWI4MzItM2U2MjJhYzlkNmEzXkEyXkFqcGdeQXVyNDAxNjkxNjQ@._V1_.jpg",
        "Plot": "Bruce Banner, a genetics researcher with a tragic past, suffers an accident that causes him to transform into a raging green monster when he gets angry.",
        "Production Companies (1st)": "Universal Pictures",
        "Title": "Hulk",
        "Title Id": "tt0286716",
        "Year of Release": 2003,
        "IMDB Rating": 5.6,
        "Runtime (Minutes)": 138.0,
        "Lead Actors": "['John Maraffi', 'David Sutherland', 'Brett Thacher', 'Kirk B.R. Woller', 'Amir Faraj', 'Craig Damon', 'Eric Ware', 'Paul Kim Jr.', 'Todd Lee Coralli', 'Sean Mahon', 'Randy Neville', 'Johnny Kastl', 'Daniel Dae Kim', 'Mike Erwin', 'Jenn Gotzon', 'Regina McKee Redwing', 'Rhiannon Leigh Wryn', 'Louanne Kelley', 'Toni Kallen', 'Rondda Holeman', 'Eva Burkley', 'Celia Weston', 'Boni Yanagisawa', 'John Littlefield', 'Josh Lucas', 'David Kronenberg', 'David St. Pierre', 'Geoffrey Scott', 'Michael Kronenberg', 'Daniella Kuhn', 'Paul Kersey', 'Sam Elliott', 'Nick Nolte', 'Cara Buono', 'Stan Lee', 'Lou Ferrigno', 'Jesse Corti', 'Ricardo Aguilar', 'Eric Bana', 'Lorenzo Callender', 'Mark Atteberry', 'Jennifer Connelly', 'Ang Lee', 'Todd Tesen', 'Rob Swanson', 'John Prosky', 'Michael Papajohn', 'Regi Davis', 'Kevin Rankin', 'Lou Richards', 'Victor Rivers']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['gets', 'past']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 251,
        "Best Picture": "None",
        "Certificate (GB)": "None",
        "Certificate (US)": "Not Rated",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BMjA5MTE2NDM5N15BMl5BanBnXkFtZTcwODU2ODk3OA@@._V1_.jpg",
        "Plot": "Amidst foreboding lighting and tremors, a traveling salesman with a dark past must fight demons, both his own and a murderous biker gang, in his quest to complete his last sale and go home.",
        "Production Companies (1st)": "Latigo Entertainment",
        "Title": "Revelation Road: The Beginning of the End",
        "Title Id": "tt2412746",
        "Year of Release": 2013,
        "IMDB Rating": 4.6,
        "Runtime (Minutes)": 88.0,
        "Lead Actors": "['Brian Bosworth', 'Laksh Singh', 'David A.R. White', 'Bruce Marchiano', 'Frederick Lawrence', 'David Pires', 'Russell Wolfe', 'Andrea Logan', 'Eliza Roberts', 'Dea Vise', 'Leticia Robles', 'Ray Wise', 'Carey Scott', 'Sean Gibney', 'Joseph Lee Michael', 'Lorin McCraley', 'Michael John Lane', 'Ocean White', 'Mavrick Von Haug', 'Ron Kari', 'Ed Hernandez', 'Steve Froehlich', 'Noell Coet', 'Sarah Prikryl', 'Ciddy Fonteboa', 'Jen Lilley', 'James Fernandez', 'Frankie Brumm', 'Ben Scott', 'Robert Miano', 'Ella Berry', 'Eric Roberts', 'Maura Murphy', 'Gabriel Sabloff', 'Monte Rex Perlin', 'Steve Borden', 'Michael Gier', \"David 'Shark' Fralick\", 'Jerry Farmer']",
        "genres": "['Action']",
        "plot_keywords": "['home', 'fight', 'past']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 10549,
        "Best Picture": "None",
        "Certificate (GB)": "18",
        "Certificate (US)": "None",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BMTgyNDkzNjA0OV5BMl5BanBnXkFtZTgwMTM1Mzc0OTE@._V1_.jpg",
        "Plot": "After X-Corp, a radical weapons manufacturer, is taken over by a Cyber Virus, a group of survivors must fight to save humanity from the army of Machines the Virus now controls.",
        "Production Companies (1st)": "Arrowstorm Entertainment",
        "Title": "Cyborg X",
        "Title Id": "tt3899262",
        "Year of Release": 2016,
        "IMDB Rating": 3.5,
        "Runtime (Minutes)": 90.0,
        "Lead Actors": "['Walter Platz', 'Adam Johnson', 'Alan Bagh', 'Rocky Myers', 'Jason K. Wixom', 'James C. Morris', 'Jake Stormoen', 'Danny James', 'Eve Mauro', 'Angie Papanikolas', 'Shona Kay', 'Anton Hawk Williams', 'Damon Wilder', 'Seth H. Steadman', 'Trevor Foisy', 'K. King', 'Brian K. Ditch', 'Aubrey Reynolds', 'Lexi Soto', 'Paul Hunt', 'Danny Trejo', 'Jill Adler']",
        "genres": "['Action', 'Horror', 'Sci-Fi']",
        "plot_keywords": "['save', 'group', 'fight']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 13609,
        "Best Picture": "None",
        "Certificate (GB)": "15",
        "Certificate (US)": "R",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BYjRiN2Y1MjctMWUxYS00YTA0LTljOTYtNDI3MzY4MjljODY4XkEyXkFqcGdeQXVyNjg0ODE2MzY@._V1_.jpg",
        "Plot": "Two years after aliens land on Earth, survivors from Sydney, Australia, fight in a desperate war as the number of casualties continue to grow.",
        "Production Companies (1st)": "Occupation Two Productions",
        "Title": "Occupation: Rainfall",
        "Title Id": "tt8615822",
        "Year of Release": 2020,
        "IMDB Rating": 4.7,
        "Runtime (Minutes)": 128.0,
        "Lead Actors": "['Geoff Imrie', 'Mark Coles Smith', 'John Reynolds', 'Elphie Coyle', 'David Roberts', \"Peter O'Hanlon\", 'Brad McMurray', 'Memphis Sargeant', 'Angel Reid', 'Luke Sparke', 'Dan Ewing', 'Zac Garred', 'Tony Nixon', 'Ben Chisholm', 'Lawrence Makoare', 'Jacob Paint', 'Dena Kaplan', 'Ken Jeong', 'David Becconsall', 'James Straiton', 'Katrina Risteska', 'Eliza Matengu', 'Izzy Stevens', 'Trystan Go', 'Rhylan Jay Bush', 'Jet Tranter', 'Tara Wraith', 'Madison Haley', 'Erin Connor', 'Sam Sidhu', 'Chloe De Los Santos', 'Jason Isaacs', 'Vince Colosimo', 'Temuera Morrison', 'Daniel Gillies']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['war', 'years', 'fight']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 12037,
        "Best Picture": "None",
        "Certificate (GB)": "15",
        "Certificate (US)": "R",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BYTViNzMxZjEtZGEwNy00MDNiLWIzNGQtZDY2MjQ1OWViZjFmXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        "Plot": "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine, sent from the same year, which has been programmed to execute a young woman whose unborn son is the key to humanity's future salvation.",
        "Production Companies (1st)": "Cinema '84",
        "Title": "The Terminator",
        "Title Id": "tt0088247",
        "Year of Release": 1984,
        "IMDB Rating": 8.1,
        "Runtime (Minutes)": 107.0,
        "Lead Actors": "['Earl Boen', 'Dick Miller', 'Bruce M. Kerner', 'Brad Rearden', 'Bill W. Richmond', 'David Michels', \"Chino 'Fats' Williams\", 'Anthony Trujillo', 'Hettie Lynne Hurtes', 'Harriet Medin', 'Bess Motta', 'Barbara Powers', 'Franco Columbu', 'Stan Yale', 'Brian Thompson', 'William Wisher', 'Webster Williams', 'Paul Winfield', 'Greg Robbins', 'Al Kahn', 'Arnold Schwarzenegger', 'Michael Biehn', 'Lance Henriksen', 'Bill Paxton', 'Linda Hamilton', 'Tony Mirelez', 'Rick Rossovich', 'James Cameron', 'James Ralston', 'John E. Bristol', 'Philip Gordon', 'Patrick Pinney', 'Loree Frazier', 'Shawn Schepps', 'Leslie Morris', 'Wayne Stone', 'Marianne Muellerleile', 'Tom Oberhaus', 'Hugh Farrington', 'Norman Friedman', 'Ken Fritz', 'Ed Dogans', 'Joe Farago', 'John Durban']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['future', 'woman', 'stop', 'son', 'year', 'young']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 3503,
        "Best Picture": "None",
        "Certificate (GB)": "15",
        "Certificate (US)": "R",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BYWM5OWIyZWEtZDJmOC00MGFmLWFhMjctMTQ4YTE5ZGM1NzY1XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_.jpg",
        "Plot": "In postapocalyptic war-torn 2073, a scientist from another timeline must help a resistance group stop the army of indestructible A.P.E.X. terminator robots he'd mistakenly created, even if it means risking erasing himself from existence.",
        "Production Companies (1st)": "Green Communications",
        "Title": "A.P.E.X.",
        "Title Id": "tt0109144",
        "Year of Release": 1994,
        "IMDB Rating": 4.3,
        "Runtime (Minutes)": 98.0,
        "Lead Actors": "['Gary Moran', 'Brian Richard Peck', 'Eric Gordon', 'Adam Lawson', 'David Jean Thomas', 'Jay Irwin', 'Gordon Capps', 'Kathleen Randazzo', 'Robert J. Marino', 'Anna B. Choi', 'Randy Kagan', 'Marklen Kennedy', 'Joe Zimmerman', 'Richard Keats', 'Tony Gugliuzza', 'Richard Hench', 'Todd James', 'Kareem H. Captan', 'J Bartell', 'Marcus Aurelius', 'Steven Michael', 'Mitchell Cox', 'Robert Tossberg', 'Jose Ontiveros', 'Merle Nicks', 'Jeffre Phillips', 'Jack Barrett Phelan', 'Lisa Ann Russell', 'Suzi Mealing', 'Tom Fellon', 'Phillip J. Roth', 'Kristin Norton', 'Natasha Roth']",
        "genres": "['Action', 'Sci-Fi']",
        "plot_keywords": "['war', 'stop', 'group', 'help']",
        "Cluster": 3
    },
    {
        "Unnamed: 0": 5852,
        "Best Picture": "None",
        "Certificate (GB)": "12",
        "Certificate (US)": "PG-13",
        "Image Url (Title)": "https://m.media-amazon.com/images/M/MV5BYWQxN2I1NjItMDVjMS00ZmJjLWIyYjItOWI2OGY5NTU1ZjI2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTc3MjM3OTA@._V1_.jpg",
        "Plot": "A sci-fi/thriller story centered on a special-ops team that is dispatched to fight supernatural beings.",
        "Production Companies (1st)": "Legendary Entertainment",
        "Title": "Spectral",
        "Title Id": "tt2106651",
        "Year of Release": 2016,
        "IMDB Rating": 6.3,
        "Runtime (Minutes)": 107.0,
        "Lead Actors": "['Louis Ozawa', 'Gonzalo Menendez', 'Cory Hardrict', 'Jimmy Akingbola', 'Clayne Crawford', 'Bruce Greenwood', 'Declan Hannigan', 'Emily Mortimer', 'Philip Bulcock', 'Zoli Teglas', \"Mark O'Neal\", 'Thomas Kelly', 'Geoffrey Thomas', 'Aaron Serban', 'Dylan Smith', 'Zalan Sipos', 'Royce Pierreson', 'Ursula Parker', 'Mike Bodie', 'Peter Schueller', 'James Badge Dale', 'Nic Mathieu', 'Stephen Root', 'Max Martini', 'Ryan Robbins']",
        "genres": "['Action', 'Adventure', 'Sci-Fi']",
        "plot_keywords": "['story', 'team', 'fight']",
        "Cluster": 3
    }
]

def get_movie_name_list_dummy():
    return[
            "Avatar",
            "Pirates of the Caribbean: At World's End",
            "Spectre",
            "The Dark Knight Rises",
            "John Carter",
            "Spider-Man 3",
            "Tangled",
            "Avengers: Age of Ultron",
        ]


def get_movie_name_list():
    print(df_model["Title"].values)
    return df_model["Title"].values

def load_kmeans_model(model_filename):
    """
    Load a KMeans model from a file.

    Args:
    model_filename (str): The filename of the saved KMeans model.

    Returns:
    KMeans: The loaded KMeans model.
    """
    return joblib.load(model_filename)


def get_movie_index(movie_title, df_model):
    """
    Returns the index of the movie in the DataFrame.

    Args:
    movie_title (str): The title of the movie.
    df_model (DataFrame): The DataFrame containing movie data.

    Returns:
    int: The index of the movie in the DataFrame.
    """
    if movie_title in df_model["Title"].values:
        return df_model[df_model["Title"] == movie_title].index[0]
    else:
        return None  # or raise an error if the movie is not found


def load_features(df_model):
    # One-hot encode genres
    mlb_genres = MultiLabelBinarizer()
    genres_encoded = mlb_genres.fit_transform(df_model["genres"])

    # One-hot encode plot keywords
    mlb_keywords = MultiLabelBinarizer()
    keywords_encoded = mlb_keywords.fit_transform(df_model["plot_keywords"])

    # Combine genres and plot keywords features
    combined_features = np.hstack((genres_encoded, keywords_encoded))
    return combined_features


def recommend_movies(target_movie_index, df_model, combined_features, top_n=5):
    # Step 2: Find the target movie's cluster
    target_cluster = df_model.loc[target_movie_index, "Cluster"]

    # Step 3: Filter movies from the same cluster
    same_cluster_movies = df_model[df_model["Cluster"] == target_cluster]

    # Step 4: Calculate cosine similarity within the cluster
    similarity_scores = cosine_similarity(
        [combined_features[target_movie_index]],
        combined_features[same_cluster_movies.index],
    )

    # Get top-N similar movies
    # Argsort returns indices that would sort an array, with the most similar at the end; [::-1] reverses it
    most_similar_indices = similarity_scores.argsort()[0][::-1][
        1 : top_n + 1
    ]  # Exclude the first one (the movie itself)

    # Step 5: Recommend similar movies
    recommended_movies = df_model.loc[same_cluster_movies.index[most_similar_indices]]
    # return recommended_movies.set_index(["Title"])
    return recommended_movies


def get_recommended_movies(movie_name="The Avengers", top_n=10, rating_range=(0.0,10.0)) -> dict:
    movie_index = get_movie_index(movie_name, df_model)
    json_str1 = df_model.iloc[movie_index].to_json( indent=4)
    json_str2 = recommend_movies(movie_index, df_model[(df_model["IMDB Rating"] >= rating_range[0]) & (df_model["IMDB Rating"] <= rating_range[1])
], combined_features, top_n=top_n).to_json(orient="records", indent=4)

    # Convert JSON strings back to Python objects
    data1 = json.loads(json_str1)
    data2 = json.loads(json_str2)

    # Combine the data into a single structure
    combined_data = [data1] + data2


    # # Convert the combined structure back to a JSON string
    return combined_data
# def get_recommended_movies(movie_name="The Avengers", top_n=10, rating_range=(0.0,10.0)) -> dict:
#     movie_index = get_movie_index(movie_name, df_model)

#     if movie_index is None:
#         raise ValueError(f"Movie '{movie_name}' not found in the dataset.")

#     # Apply IMDb rating filter
#     filtered_df = df_model[(df_model["IMDB Rating"] >= rating_range[0]) & (df_model["IMDB Rating"] <= rating_range[1])]

#     # Ensure there are enough movies for recommendations
#     if len(filtered_df) < top_n + 1:
#         if top_n > 1:
#             return get_recommended_movies(movie_name, top_n - 1, rating_range)
#         else:
#             raise ValueError("Unable to find enough movies for recommendations.")

#     try:
#         # Proceed with recommendations
#         json_str1 = df_model.iloc[movie_index].to_json(indent=4)
#         json_str2 = recommend_movies(movie_index, filtered_df, combined_features, top_n=top_n).to_json(orient="records", indent=4)

#         # Convert JSON strings back to Python objects
#         data1 = json.loads(json_str1)
#         data2 = json.loads(json_str2)

#         # Combine the data into a single structure
#         combined_data = [data1] + data2
#         return combined_data
#     except Exception as e:
#         # If an exception occurs, try with a smaller top_n
#         if top_n > 1:
#             return get_recommended_movies(movie_name, top_n - 1, rating_range)
#         else:
#             raise ValueError("Unable to find enough movies for recommendations.")


# def get_recommended_movies(movie_name="The Avengers", top_n=10, rating_range=(0.0,10.0)) -> dict:
#     # Get the index of the movie
#     movie_index = get_movie_index(movie_name, df_model)
#     if movie_index is None:
#         raise ValueError(f"Movie '{movie_name}' not found in the dataset.")

#     # Apply IMDb rating filter
#     filtered_df = df_model[(df_model["IMDB Rating"] >= rating_range[0]) & (df_model["IMDB Rating"] <= rating_range[1])]

#     # Check if there are enough movies for recommendations
#     if top_n <= 0 or len(filtered_df) < top_n:
#         raise ValueError("Unable to find enough movies for recommendations.")

#     try:
#         # Proceed with recommendations
#         json_str1 = df_model.iloc[movie_index].to_json(indent=4)
#         recommended_movies_df = recommend_movies(movie_index, filtered_df, combined_features, top_n=top_n)

#         # Check if the recommended movies dataframe is empty or the movie itself is the only one found
#         if recommended_movies_df.empty or (len(recommended_movies_df) == 1 and recommended_movies_df.iloc[0].name == movie_index):
#             raise ValueError("No suitable recommendations found.")

#         json_str2 = recommended_movies_df.to_json(orient="records", indent=4)

#         # Convert JSON strings back to Python objects
#         data1 = json.loads(json_str1)
#         data2 = json.loads(json_str2)

#         # Combine the data into a single structure
#         combined_data = [data1] + data2
#         return combined_data
#     except Exception as e:
#         # If an exception occurs or no suitable recommendations, try with a smaller top_n
#         return get_recommended_movies(movie_name, top_n - 1, rating_range)








# Define the directory paths
foldername = 1
directory = f"model/{foldername}"
model_filename = "kmeans_model.pkl"
df_model_filename = "movie_data.csv"
combined_features_filename = "combined_features.pkl"

# Load model from the file
kmeans_model = load_kmeans_model(os.path.join(directory, model_filename))
# Load df_model from the file
df_model = pd.read_csv(os.path.join(directory, df_model_filename))
combined_features = load_features(df_model)


if __name__ == "__main__":
    target_movie_title = "The Avengers"

    # index_of_search_movie = get_movie_index(target_movie_title, df_model)

    # # # Access the row corresponding to the targemovie
    # target_movie_row = df_model.iloc[index_of_search_movie]

    # recommended_movies = get_recommended_movies(target_movie_title)

    # print(target_movie_row)
    # print(recommended_movies)
    x = get_recommended_movies(target_movie_title)
    # Print the JSON string
    # print(x)
    print(json.dumps(x, indent=4))
    print(len(x))
