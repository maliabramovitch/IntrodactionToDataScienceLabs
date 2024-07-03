import pandas as pd

"""
PART 01
"""

# QU 01
data = pd.read_csv('2014.results.txt', delimiter='\t', header=0)
data['Goals_home'] = data['Goals_home'].apply(int)
data['Goals_away'] = data['Goals_away'].apply(int)

# QU 02
max_i_goals_home = pd.Series.argmax(data['Goals_home'])
home_team = data.iloc[max_i_goals_home]['Home']
home_score = data.iloc[max_i_goals_home]['Goals_home']
away_team = data.iloc[max_i_goals_home]['Away']
print('--- QU 02 ---')
print(f"The max score for home team: {home_team} with {home_score} goals against {away_team}")
print()

# QU03
max_i_goals_away = pd.Series.argmax(data['Goals_away'])
away_team = data.iloc[max_i_goals_away]['Away']
away_score = data.iloc[max_i_goals_away]['Goals_away']
print('--- QU 03 ---')
if away_score > home_score:
    home_team = data.iloc[max_i_goals_away]['Home']
    print(f"The max score for all teams: {away_team} (Away) with {away_score} goals against {home_team} (Home)")

else:
    print(f"The max score for all teams: {home_team} (Home) with {home_score} goals against {away_team} (Away)")
print()

# QU04
home_mean_score = data['Goals_home'].mean()
away_mean_score = data['Goals_away'].mean()
print('--- QU 04 ---')
print(f"The mean for home teams score is: {home_mean_score}")
print(f"The mean for away teams score is: {away_mean_score}")
print()

# QU05
home_wins = (data['Goals_home'] > data['Goals_away']).sum()
away_wins = (data['Goals_home'] < data['Goals_away']).sum()
ties = (data['Goals_home'] == data['Goals_away']).sum()
print('--- QU 05 ---')
print(f"Home wins = {home_wins}    Away wins = {away_wins}   Ties = {ties}")
print()

# QU06
alls = data.groupby('Home')['Goals_home'].sum() + data.groupby('Away')['Goals_away'].sum()
print('--- QU 06 ---')
print(alls)
print()

# QU07
homes = data.groupby('Home').apply(lambda row: (row['Goals_home'] + row['Goals_away']).sum())
print('--- QU lab07 ---')
print(homes)
print()

"""
PART 02
"""
print('--- PART 2 ---')
data2 = pd.DataFrame(index=alls.index, columns=['Wins', 'Ties', 'Losses', 'GF', 'GA', 'Points'])
data2.fillna(0, inplace=True)
for row in data.itertuples():
    home_team, away_team, home_score, away_score = row[1], row[2], row[3], row[4]

    if home_score > away_score:
        data2.loc[home_team, 'Wins'] += 1
        data2.loc[home_team, 'GF'] += home_score
        data2.loc[home_team, 'Points'] += 3
        data2.loc[away_team, 'Losses'] += 1
        data2.loc[away_team, 'GA'] += home_score
    elif home_score < away_score:
        data2.loc[away_team, 'Wins'] += 1
        data2.loc[away_team, 'GF'] += away_score
        data2.loc[away_team, 'Points'] += 3
        data2.loc[home_team, 'Losses'] += 1
        data2.loc[home_team, 'GA'] += away_score
    else:
        data2.loc[home_team, 'Ties'] += 1
        data2.loc[home_team, 'Points'] += 1
        data2.loc[home_team, 'GF'] += home_score
        data2.loc[home_team, 'GA'] += away_score
        data2.loc[away_team, 'Ties'] += 1
        data2.loc[away_team, 'Points'] += 1
        data2.loc[away_team, 'GF'] += away_score
        data2.loc[away_team, 'GA'] += home_score
data2.sort_values(inplace=True, by=['Points'
                                    ''], axis='rows', ascending=False)
data2.to_csv('soccer_result.csv')
print(data2)
