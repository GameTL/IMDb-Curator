from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pydantic import BaseModel, ValidationError, validator

driver = webdriver.Firefox()

def get_imdb_synopsis(driver, url):
    # Set up the Selenium WebDriver
    # driver = webdriver.Chrome(executable_path="chromedriver")


    # Go to the IMDb synopsis page
    driver.get(url)

    # Wait for the synopsis content to load
    synopsis_divs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'ipc-html-content-inner-div'))
    )
    # movie_name_divs = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'sc-a885edd8-9 dcErWY'))
    # )

    # Extract and return the text of the last synopsis div
    return synopsis_divs[-1].text if synopsis_divs else "No synopsis divs found." #, movie_name_divs[0].text if movie_name_divs else "No movie name found."

# Usage
if __name__ == "__main__":

    imdb_url = 'https://www.imdb.com/title/tt1517268/plotsummary/?ref_=tt_stry_pl'
    get_imdb_synopsis(driver, imdb_url)
    get_imdb_synopsis(driver, "https://www.imdb.com/title/tt1517268/")

    # synopsis = get_imdb_synopsis(imdb_url)
    # movie = Movie(name = "Barbie", synopsis=synopsis)
    # print(movie.model_dump_json())
