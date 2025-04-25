# Import dependencies
import pandas as pd
from consolidate_div_data import consolidate_div_data

def store_div_data(team_df: pd.DataFrame) -> None: 
    """
    Creates and saves the team standings dataframe
    to a CSV file

    Raises:
        - Any unexpected exceptions

    Args:
        team_df (pd.DataFrame): The mvp dataframe to be saved

    Returns:
        None
    """
    try: 
        # Save dataframe to CSV
        team_df.to_csv("../../data/team_csv_data/team_data.csv", index=False)
    except Exception as e: 
        print(f"Failed to save dataframe to CSV : {e}")

if __name__ == "__main__": 

    # Consolidate data
    team_data = consolidate_div_data()

    # Store data
    store_div_data(team_data)