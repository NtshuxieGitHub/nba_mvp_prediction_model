# Import dependencies
import pandas as pd

def mvp_data_cleaning() -> pd.DataFrame:
    """
    Loads and cleans the MVP stats data

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The cleaned MVP dataframe
    """
    try: 
        # Set mvp csv path
        mvp_csv_path = '../../data/mvp_csv_data/mvp_data.csv'

        # Load csv file into a datafram
        mvp_df = pd.read_csv(mvp_csv_path)

        # Filter out data to contain desired/useful columns
        mvp_df = mvp_df[["Player", "Year", "Pts Won", "Pts Max", "Share"]]

        # Return cleaned df 
        return mvp_df
        
    except Exception as e: 
        print(f"Failed to load and clean dataframe : {e}")