# Import dependencies
import pandas as pd
from sklearn.linear_model import Ridge
import os
import sys
from typing import Tuple
from backtest import backtest

# Add root config folder to sys.path
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
sys.path.append(config_path)

# Import variables from config.py
from config import prediction_years, predictors

# Add 'src/data_processing' folder to sys.path for data_processing import
data_processing_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'data_processing'))
sys.path.append(data_processing_path)

# Import variables from data_processing.py
from data_processing import data_processing

def modelling():
    """
    Modelling
    """
    try:
        # Initialize model with a regularization strength of 0.1
        reg = Ridge(alpha=0.1)

        # Load and process data
        stats = data_processing()

        # Backtest
        mean_aps, aps, predictions = backtest(stats, reg, prediction_years, predictors)

        return mean_aps, aps, predictions

    except Exception as e:
        print(f"failed to model : {e}")
        return None, None, None

