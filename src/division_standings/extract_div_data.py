# Import dependencies
from bs4 import BeautifulSoup
import pandas as pd
from typing import List
import sys
import os
from io import StringIO

# Add root config folder to sys.path
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
sys.path.append(config_path)

# Import variables from config.py
from config import years

def extract_div_data() -> List[pd.DataFrame]:
    """
    Extracts NBA MVP data from locally saved HTML files 
    for a range of NBA seasons

    Raises:
        Prints detailed error messages for:
        - No MVP table is found in html page
        - Missing or unreadable files
        - HTML parsing issues
        - Missing tables
    
    Returns:
        List: A list of pandas dataframes, for for each year
    """
    # Initialise mvp dataframes
    mvp_dfs = []

    for year in years:

        # get html file path
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data/mvp_data', f'{year}.html'))

        try:
            # Read html pages
            with open(file_path, encoding='utf-8') as readData:
                    
                # Read html page
                page = readData.read()

                # Parse html page using html parser
                soup = BeautifulSoup(page, 'html.parser')

                # Decompose the html soup
                over_header = soup.find('tr', class_='over_header')
                if over_header:
                    over_header.decompose()

                # Find the table with the MVP data using the unique html identifier
                mvp_table = soup.find(id="mvp")
                if not mvp_table:
                    raise ValueError(f"No MVP table found in file for year {year}")

                # Read the html table into a dataframe using pandas
                mvp_dataframe = pd.read_html(StringIO(str(mvp_table)))[0]

                # Create a Year column for tracking
                mvp_dataframe["Year"] = year

                # Write data to mvp_dfs
                mvp_dfs.append(mvp_dataframe)

        except FileNotFoundError as fe:
            print(f"File not found for year {year} : {fe}")
        except ValueError as ve:
            print(f"{ve}")
        except Exception as e:
            print(f"Unexpected error while processing {year} : {e}")

    # Return mvp_dfs
    return mvp_dfs

        