# Import dependencies
import pandas as pd
from consolidate_data import consolidate_data

def store_div_data(mvp_df: pd.DataFrame) -> None: 
    """
    Creates and saves the mvp dataframe to a CSV file

    Raises:
        - Any unexpected exceptions

    Args:
        mvp_df (pd.DataFrame): The mvp dataframe to be saved

    Returns:
        None
    """
    try: 
        # Save dataframe to CSV
        mvp_df.to_csv("../../data/mvp_csv_data/mvp_data.csv", index=False)
    except Exception as e: 
        print(f"Failed to save dataframe to CSV : {e}")

if __name__ == "__main__": 

    # Consolidate data
    data = consolidate_data()

    # Store data
    store_data(data)