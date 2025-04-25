# Import dependencies
from extract_div_data import extract_div_data
import pandas as pd

def consolidate_div_data() -> pd.DataFrame:
    """
    Uses the extract_team_data function to 
    extract data from the HTML files and 
    consolidates the East and West standings 
    dataframes from each year to form a single 
    dataframe of data

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The consolidated NBA standings dataframe
    """
    try:
        # Use extract_data to extract HTML data
        team_dfs = extract_div_data()

        # Concatenate dataframes
        team_df = pd.concat(team_dfs)

        return team_df
    except Exception as e:
        print(f"Failed to consolidate dataframes : {e}")