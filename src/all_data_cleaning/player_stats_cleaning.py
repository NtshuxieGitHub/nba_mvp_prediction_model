# Import dependencies
import pandas as pd
from single_row import single_row

def player_stats_cleaning() -> pd.DataFrame:
    """
    Loads and cleans the player stats data

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The cleaned player dataframe
    """
    try:
        # Set player csv path
        player_csv_path = '../../data/player_csv_data/player_data.csv'

        # Load csv file into a dataframe
        player_df = pd.read_csv(player_csv_path)

        # Remove useless columns
        del player_df['Rk']

        # Remove asterisk in some of the player names in player_df
        player_df['Player'] = player_df['Player'].str.replace('*', '', regex=False)

        # For player with multiple row entries, use the total 
        # row and remove the other rows
        player_df = player_df.groupby(["Player", "Year"]).apply(single_row)

        # Drop index levels added by grouping the player data 
        player_df.index = player_df.index.droplevel()
        player_df.index = player_df.index.droplevel()

        return player_df

    except Exception as e:
        print(f"Failed to load and clean dataframe : {e}")