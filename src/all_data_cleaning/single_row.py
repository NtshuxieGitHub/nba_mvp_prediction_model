# Import dependencies
import pandas as pd

def single_row(df: pd.DataFrame) -> pd.DataFrame:
    """
    For player with multiple row entries, use the total 
    row and remove the other rows

    Args:
        df (pd.DataFrame): The dataframe to be cleaned

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The cleaned dataframe
    """
    try:
        if df.shape[0] == 1:
            # If there is only one row for player in year, 
            # then return that row

            return df
        else:
            # If there are multiple rows for player in year, 
            # then return the total row and remove the other rows

            row = df[df["Team"] == "TOT"]
            row["Team"] = df.iloc[-1,:]
            return row

    except Exception as e:
        print(f"Failed to extract total player stats row for year : {e}")    