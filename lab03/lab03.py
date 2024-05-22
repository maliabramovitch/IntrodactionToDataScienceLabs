import pandas as pd

# QU 01
data = pd.read_csv('2014.results.txt', delimiter='\t', header=0)
data['Goals_home'] = data['Goals_home'].apply(int)
data['Goals_away'] = data['Goals_away'].apply(int)

# QU 02
max_i_goals_home = pd.Series.argmax(data['Goals_home'])
home_team = data.iloc[max_i_goals_home]['Home']
home_score = data.iloc[max_i_goals_home]['Goals_home']
away_team = data.iloc[max_i_goals_home]['Away']
print(f"The max score for home team: {home_team} with {home_score} goals against {away_team}")

# QU03
max_i_goals_away = pd.Series.argmax(data['Goals_away'])
away_team = data.iloc[max_i_goals_away]['Away']
away_score = data.iloc[max_i_goals_away]['Goals_away']

if away_score > home_score:
    home_team = data.iloc[max_i_goals_away]['Home']
    print(f"The max score for all teams: {away_team} (Away) with {away_score} goals against {home_team} (Home)")
else:
    print(f"The max score for all teams: {home_team} (Home) with {home_score} goals against {away_team} (Away)")

# QU04
home_mean_score = data['Goals_home'].mean()
away_mean_score = data['Goals_away'].mean()
print(f"The mean for home teams score is: {home_mean_score}")
print(f"The mean for away teams score is: {away_mean_score}")

# QU05
home_wins = data.loc[(data['Goals_home'] > data['Goals_away'])]
away_wins = 0
ties = 0
home_team, away_team, home_score, away_score = 0, 0, 0, 0
for row in data.itertuples():
    home_team, away_team, home_score, away_score = row[1], row[2], row[3], row[4]
    if home_score == away_score:
        ties += 1
    elif home_score > away_score:
        home_wins += 1
    else:
        away_wins += 1
print(f"Home wins = {home_wins}    Away wins = {away_wins}   Ties = {ties}")
