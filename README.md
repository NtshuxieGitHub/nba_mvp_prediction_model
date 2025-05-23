# 🏀 NBA MVP Prediction using Python

This project aims to predict NBA Most Valuable Player (MVP) voting share and rank for players using machine learning. Two models were used: Ridge Regression and Random Forest Regressor, with the latter serving as a performance improvement over the baseline.

## 📌 Project Overview

The objective was to build a model that could estimate a player's MVP voting share and rank based on their season performance and team success. The end-to-end pipeline includes data scraping, preprocessing, exploratory data analysis (EDA), feature engineering, model training, and evaluation.

## ⚙️ Workflow

1. **Web Scraping (BeautifulSoup & Selenium):**

   - Collected MVP voting data, player season statistics, and team standings from Basketball Reference.
   - Used both BeautifulSoup and Selenium depending on the structure and complexity of the pages.

2. **Data Consolidation:**

   - Merged individual datasets into a single cleaned dataframe for modeling.

3. **Exploratory Data Analysis (EDA):**

   - Analyzed trends, distributions, and feature correlations to gain insights and identify relevant predictors.

4. **Feature Engineering:**

   - Created additional features such as team rankings, position/team encoding, and performance ratios to enhance model input.

5. **Machine Learning Models:**

   - **Ridge Regression:** Baseline model for MVP share prediction.
   - **RandomForestRegressor:** Improved model with non-linear capability and better accuracy.

6. **Prediction Accuracy Testing:**

   - Used a custom backtest function to evaluate prediction accuracy across multiple seasons.
   - Assessed model performance using mean average precision and visual inspection.

7. **Model Diagnosis and Improvement:**
   - Identified model weaknesses using diagnostics, improved features, and handled edge cases (e.g., division by zero, missing values).

## 🧠 Tech Stack

- **Language:** Python
- **Web Scraping:** BeautifulSoup, Selenium
- **Data Handling:** Pandas
- **Machine Learning:** scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Environment:** Jupyter Notebooks (.ipynb) and Python modules (.py)

## 🛠 Structure

    - /: exploratory_data_analysis.ipynb, and machine_learning.ipynb
    - src/: folders for automated scraping, data consolidation, cleaning and machine learning
    - config/: Configurable settings (e.g., predictor columns, year ranges, etc)
    - data/: saved data from scraping and processing/cleaning saved in .html or .csv formats

## ✅ Key Takeaways

- Successfully predicted MVP outcomes using historical performance data with an accuracy of as high as 93%.
- Demonstrated the value of automated ML pipelines for sports analytics.
- Gained hands-on experience with web scraping, EDA, feature engineering, and backtesting.
