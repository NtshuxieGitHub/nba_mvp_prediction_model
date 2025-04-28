# Year range 
years = list(range(1994, 2024))

# Data scraping url
url = "https://www.basketball-reference.com/awards/awards_{}.html"

# Player stats url
stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

# Team stats url
team_url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html"

# Configs for data split
part1 = slice(0, 45)
part2 = slice(52745, 65110)

# Set a list of predictore columns using the list of columns from df
predictors = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA',
    '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 
    'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year', 'W', 'L', 
    'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']

prediction_years = years[5:]

