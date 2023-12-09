import requests
from bs4 import BeautifulSoup

def extract_synopsis(imdb_url):
    response = requests.get(imdb_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding the synopsis section
    synopsis_section = soup.find('ul', {'id': 'plot-synopsis-content'})
    if synopsis_section:
        synopsis = synopsis_section.get_text(strip=True)
        return synopsis
    else:
        return "Synopsis not found."

# IMDb URL for 'Avengers: Endgame'
url = 'https://www.imdb.com/title/tt4154796/plotsummary/'
print(extract_synopsis(url))
