# Import dependencies
import pandas as pd
import os
import sys

# Add the ROOT folder (2 levels up from machine_learning)
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
sys.path.append(config_path)

# Now this works
from config import part1, part2

def data_processing() -> pd.DataFrame:
    """
    Processes the stats data

    Raises:
        - Any unexpected exceptions

    Returns:
        pd.DataFrame: The processed dataframe
    """
    try:
        # Set path for consolidated data
        file_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'merged_excel_data.csv'))

        # Load csv file into a dataframe
        df = pd.read_csv(file_path, low_memory=False)

        # Split the data using configs
        df1 = df.iloc[part1]
        df2 = df.iloc[part2]

        # Combine extracted data and reset indices
        new_df = pd.concat([df1, df2])
        new_df.reset_index(drop=True, inplace=True)

        # Save modified dataframe
        new_df.to_csv("../../data/cleaned_data.csv", index=False)
        stats = new_df

        # Fill missing values with 0
        stats.fillna(0, inplace=True)
        stats.to_csv("../../data/cleaned_data_for_ml.csv", index=False)

        # Remove all rows where year is 0
        stats = stats[stats["Year"] != 0]
        print(stats.shape)

        return stats
    except  Exception as e: 
        print(f"Failed to process NBA stats data : {e}")