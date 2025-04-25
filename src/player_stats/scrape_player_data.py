# Import dependencies
import requests as rqs
import sys
import os
import time

# Add root config folder to sys.path
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
sys.path.append(config_path)

# Import variables from config.py
from config import years, stats_url

# impport selenium and webdriver dependencies
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

def scrape_player_data():
    """
    Scrapes player statistics from basketball-reference.com

    Raises: 
        Prints detailed error messages for:
        - Network-related errors (connection issues, timeouts, etc.)
        - Invalid HTTP responses (e.g., 404 not Found)
        - File system issue (permission denied, invalid path)
        - Any unexpected exceptions
    """
    try:
        # Initialize webdriver
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        for year in years:

            # Set url for year
            url = stats_url.format(year)

            # Get html page
            driver.get(url)
            driver.execute_script("window.scrollTo(1, 10000)")

            # Set timer
            time.sleep(3)

            # Get html page
            html_page = driver.page_source

            # Save html page
            with open("../../data/player_data/{}.html".format(year), "w+", encoding="utf-8") as writeData:
                writeData.write(driver.page_source)

        # Close webdriver
        driver.quit()
    except rqs.exceptions.RequestException as e:
        print(f"Request failed for {year} : {e}")
    except OSError as e:
        print(f"File error while saving {year} : {e}")
    except Exception as e:
        print(f"Unexpected error for {year} : {e}")

if __name__ == "__main__": 
    scrape_player_data()