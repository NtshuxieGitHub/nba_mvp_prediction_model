# Import dependencies
import pandas as pd
from consolidate_player_data import consolidate_player_data

def store_player_data(player_df: pd.DataFrame) -> None: 
    """
    Creates and saves the player dataframe to a CSV file

    Raises:
        - Any unexpected exceptions

    Args:
        mvp_df (pd.DataFrame): The mvp dataframe to be saved

    Returns:
        None
    """
    try: 
        # Save dataframe to CSV
        player_df.to_csv("../../data/player_csv_data/player_data.csv", index=False)
    except Exception as e: 
        print(f"Failed to save dataframe to CSV : {e}")

if __name__ == "__main__": 

    # Consolidate data
    player_data = consolidate_player_data()

    # Store data
    store_player_data(player_data)