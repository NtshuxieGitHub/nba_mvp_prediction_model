# Import dependencies
from player_stats_cleaning import player_stats_cleaning
from mvp_data_cleaning import mvp_data_cleaning
from team_data_cleaning import team_data_cleaning
import pandas as pd

def merge_data() -> None:
    """
    Merges the player and mvp dataframes

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The merged dataframe
    """
    try:
        # Run player_data_cleaning and mvp_data_cleaning
        player_df = player_stats_cleaning()
        mvp_df = mvp_data_cleaning()

        # Merge the player and mvp dataframes
        merged_df = player_df.merge(mvp_df, on=["Player", "Year"], how="outer")

        # Further process Share, Pts Max and Pts Won columns for playes 
        # who have never had any MVP votes. This is because these stats will 
        # be NaN for those players
        merged_df[["Pts Max", "Pts Won", "Share"]] = merged_df[["Pts Max", "Pts Won", "Share"]].fillna(0, inplace=True)

        # Map abbreviated team names to the team_df
        abbreviations = {}

        # Open the teams_config.csv file
        with open("../../config/teams_config.csv") as f:

            # Read all the lines in the file
            lines = f.readlines()

            # For each line - skip the header
            for line in lines[1:]:

                # Replace the backslash in the line with "". 
                # Split the line using the ; that is in the data
                abbrev, name = line.replace("\n", "").split(";")
                abbreviations[abbrev] = name

        # Map the team names to the team_df
        merged_df["Team"] = merged_df["Team"].map(abbreviations)

        # Load and clean team data
        team_df = team_data_cleaning()

        # Combine merged_df with team_df
        stats = merged_df.merge(team_df, how="outer", on=["Year", "Team"])

        # Convert some columns to numerical
        stats = stats.apply(pd.to_numeric, errors="ignore")

        # Replace "-" in GB column with 0: This means that the team 
        # was 0 games behind the first seed. Afterwards, the column 
        # is converted to a float
        stats["GB"] = stats["GB"].str.replace("—", "0")
        stats["GB"] = pd.to_numeric(stats["GB"])

        stats.to_csv("../../data/merged_data.csv", index=False)
        # return merged_df

    except Exception as e:
        print(f"Failed to merge dataframes : {e}")

if __name__ == "__main__": 
    merge_data()