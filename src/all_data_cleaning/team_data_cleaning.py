# Import dependencies
import pandas as pd

def team_data_cleaning() -> pd.DataFrame:
    """
    Cleans the team data dataframe

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The cleaned team data dataframe
    """
    try:
        # Read in the data from the CSV file
        team_df = pd.read_csv("../../data/team_csv_data/team_data.csv")

        # Get rid of rows that have "Division" in the "W" column. W is Wins
        team_df = team_df[~team_df["W"].str.contains("Division")]

        # Remove asteriks in team names
        team_df['Team'] = team_df['Team'].str.replace('*', '', regex=False)

        return team_df
        
    except Exception as e:
        print(f"Failed to load and clean dataframe : {e}")