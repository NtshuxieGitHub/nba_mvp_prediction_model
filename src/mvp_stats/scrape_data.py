# Import dependencies
import requests as rqs
import sys
import os

# Add root config folder to sys.path
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
sys.path.append(config_path)

# Import variables from config.py
from config import years, url

def scrape_data():
    """ 
    Scrapes NBA data from basketball-reference in HTML format 
    for a specified ranges of, and saves each year's pages as 
    an individual HTML in the mvp_data folder in the root folder

    Raises: 
        Prints detailed error messages for:
        - Network-related errors (connection issues, timeouts, etc.)
        - Invalid HTTP responses (e.g., 404 not Found)
        - File system issue (permission denied, invalid path)
        - Any unexpected exceptions
    """
    try:
        for year in years:

            # Download the data from the webpage
            current_url = url.format(year)
            data = rqs.get(current_url)

            # Save the data for the current year
            with open("../../data/mvp_data/{}.html".format(year), "w+", encoding="utf-8") as writeData:
                writeData.write(data.text)
    except rqs.exceptions.RequestException as e:
        print(f"Request failed for {year} : {e}")
    except OSError as e:
        print(f"File error while saving {year} : {e}")
    except Exception as e:
        print(f"Unexpected error for {year} : {e}")

# Execute
if __name__ == "__main__":
    scrape_data()