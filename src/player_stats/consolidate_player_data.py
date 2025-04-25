# Import dependencies
from process_player_data import process_player_data
import pandas as pd

def consolidate_player_data() -> pd.DataFrame:
    """
    Uses the process_player_data function to 
    remove unwanted/repeated columns, extract 
    player stats data from the HTML files and 
    consolidates the player dataframes from each 
    year to form a single dataframe of data

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The consolidated player dataframe
    """
    try:
        # Use extract_data to extract HTML data
        player_dfs = process_player_data()

        # Concatenate dataframes
        player_df = pd.concat(player_dfs)

        return player_df
    except Exception as e:
        print(f"Failed to consolidate dataframes : {e}")