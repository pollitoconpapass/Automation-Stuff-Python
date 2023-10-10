import pandas as pd

df_premier23 = pd.read_csv('https://football-data.co.uk/mmz4281/2324/E0.csv')

# === RENAMING COLUMNS ===
df_premier23.rename(columns = {'FTHG':'HomeGoals', 
                               'FTAG':'AwayGoals'}, inplace=True)
print(df_premier23)


