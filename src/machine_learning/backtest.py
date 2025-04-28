# Import dependencies
import pandas as pd
from typing import Tuple
from find_aps import find_ap
from add_ranks import add_ranks

def backtest(stats, model, years, predictors):
    """
    Backtest
    """
    # Initialize variables
    aps = []
    all_predictions = []
    
    try:
        # Loop through each year
        for year in years[5:]:

            # Create train split
            train = stats[stats["Year"] < year]

            # Create test split
            test = stats[stats["Year"] == year]

            # Back testing predictions
            model.fit(train[predictors], train["Share"])
            predictions = model.predict(test[predictors])
            predictions = pd.DataFrame(predictions, columns=["predictions"], index=test.index)
            combination = pd.concat([test[["Player", "Share"]], predictions], axis=1)

            # Return preditions for all the years
            all_predictions.append(combination)

            # Use the add_ranks function
            all_predictions.append(add_ranks(combination))
            
            # Find the average precision
            aps.append(find_ap(combination))

        # Flatten list of lists
        aps_flat = [item for sublist in aps for item in sublist]

        # Calculate overall precision of the predictions
        result = sum(aps_flat) / len(aps_flat)
        
        # Return mean average precision
        return result, aps, pd.concat(all_predictions)

    except Exception as e:
        print(f"failed to backtest : {e}")
        return None, None, None
