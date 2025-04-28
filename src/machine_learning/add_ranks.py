# Import dependencies
import pandas as pd

def add_ranks(combination: pd.DataFrame) -> pd.DataFrame:
    """
    Add ranks
    """
    try:
        # Sort rows in commbination based on Share from highest to smallest
        combination = combination.sort_values("Share", ascending=False)
        
        # Create a column Rk with the rank of the players (mvps)
        combination["Rk"] = list(range(1, combination.shape[0] + 1))

        # Sort rows in commbination based on predictions from highest to smallest
        combination = combination.sort_values("predictions", ascending=False)
        
        # Create a column Predicted_Rk with the rank of the predictions
        combination["Predicted_Rk"] = list(range(1, combination.shape[0] + 1))

        # Difference between ranks
        combination["Diff"] = combination["Rk"] - combination["Predicted_Rk"]
        
        return combination

    except Exception as e:
        print(f"failed to add ranks : {e}")