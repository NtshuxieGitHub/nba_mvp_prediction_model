# Import dependencies
from extract_data import extract_data
import pandas as pd

def consolidate_data() -> pd.DataFrame:
    """
    Uses the extract_data function to 
    extract data from the HTML files and 
    consolidates the mvp dataframes from each 
    year to form a single dataframe of data

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The consolidated mvp dataframe
    """
    try:
        # Use extract_data to extract HTML data
        mvp_dfs = extract_data()

        # Concatenate dataframes
        mvp_df = pd.concat(mvp_dfs)

        return mvp_df
    except Exception as e:
        print(f"Failed to consolidate dataframes : {e}")