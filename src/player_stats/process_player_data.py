# Import dependencies
import sys
import os
from bs4 import BeautifulSoup
import pandas as pd
from typing import List
from io import StringIO

# Add root config folder to sys.path
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
sys.path.append(config_path)

# Import variables from config.py
from config import years

def process_player_data() -> List[pd.DataFrame]:
    """
    Removes unwanted headers from player statistics 
    HTML files and creates a list of player dataframes

    aises:
        Prints detailed error messages for:
        - No MVP table is found in html page
        - Missing or unreadable files
        - HTML parsing issues
        - Missing tables

    Returns:
        List: A list of pandas dataframes, for for each year
    """
    # Initialise player dataframes
    player_dfs = []

    for year in years:

        try:

            # open html file
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data/player_data', f'{year}.html'))
            with open(file_path, encoding='utf-8') as readData:

                # read html page
                page = readData.read()

                # parse html
                soup = BeautifulSoup(page, 'html.parser')

                ## Decompose the html soup
                over_header = soup.find('tr', class_='thead')
                if over_header:
                    over_header.decompose()

                # Find the table with the player stats data using the unique html identifier
                player_table = soup.find(id="per_game_stats")
                if not player_table:
                    raise ValueError(f"No player data table found in file for year {year}")

                # Read the html table into a dataframe using pandas
                player_dataframe = pd.read_html(StringIO(str(player_table)))[0]

                # Create a Year column for tracking
                player_dataframe["Year"] = year

                # Write data to player_dfs
                player_dfs.append(player_dataframe)

        except FileNotFoundError as fe:
            print(f"File not found for year {year} : {fe}")
        except ValueError as ve:
            print(f"{ve}")
        except Exception as e:
            print(f"Unexpected error while processing {year} : {e}")

    # Return player_dfs
    return player_dfs

