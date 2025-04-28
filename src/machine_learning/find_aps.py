# Import libraries
import pandas as pd

def find_ap(combination: pd.DataFrame) -> list:
    """
    Find prediction precision
    """
    try:
        # Get the actual Share values
        actual = combination.sort_values("Share", ascending=False).head(5)

        # Get the predicted share values
        predicted = combination.sort_values("predictions", ascending=False).head(5)

        # Initialize variables
        ps = []
        found = 0
        seen = 1

        # Loop through each row in predicted
        for idx, row in predicted.iterrows():
            if row["Player"] in actual["Player"].values:
                # If the player in predicted is in actual

                # Increment found by 1 (credit for a correct prediction)
                found += 1

                # Append the found/seen ratio to ps
                ps.append(found/seen)
            
            # Increment seen by 1 
            seen += 1
        
        # Return ps
        return ps

    except Exception as e:
        print(f"failed to find ap : {e}")