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
    Extracts NBA team standings stats data from 
    locally saved HTML files for a range of NBA 
    seasons

    Raises:
        Prints detailed error messages for:
        - No team stats table is found in html page
        - Missing or unreadable files
        - HTML parsing issues
        - Missing tables
    
    Returns:
        List: A list of pandas dataframes, for for each year
    """
    # Initialise team dataframes
    team_dfs = []

    for year in years:

        # get html file path
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data/team_data', f'{year}.html'))

        try:
            # Read html pages
            with open(file_path, encoding='utf-8') as readData:
                    
                # Read html page
                page = readData.read()

            # Process and extract East Conference Standings
            soup = BeautifulSoup(page, 'html.parser')
            over_header = soup.find('tr', class_='thead')
            if over_header:
                over_header.decompose()
            team_table = soup.find(id="divs_standings_E")
            if not team_table:
                raise ValueError(f"No East standings table found in file for year {year}")
            team_dataframe = pd.read_html(StringIO(str(team_table)))[0]
            team_dataframe["Year"] = year
            team_dataframe["Team"] = team_dataframe["Eastern Conference"]
            del team_dataframe["Eastern Conference"]
            team_dfs.append(team_dataframe)

            # Process and extract East Conference Standings
            soup = BeautifulSoup(page, 'html.parser')
            over_header = soup.find('tr', class_='thead')
            if over_header:
                over_header.decompose()
            team_table = soup.find(id="divs_standings_W")
            if not team_table:
                raise ValueError(f"No West standings table found in file for year {year}")
            team_dataframe = pd.read_html(StringIO(str(team_table)))[0]
            team_dataframe["Year"] = year
            team_dataframe["Team"] = team_dataframe["Western Conference"]
            del team_dataframe["Western Conference"]
            team_dfs.append(team_dataframe)

        except FileNotFoundError as fe:
            print(f"File not found for year {year} : {fe}")
        except ValueError as ve:
            print(f"{ve}")
        except Exception as e:
            print(f"Unexpected error while processing {year} : {e}")

    # Return team_dfs
    return team_dfs

        