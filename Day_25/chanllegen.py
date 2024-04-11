import pandas as pd
df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrel = len(df[df['Primary Fur Color'] == 'Gray'])
red_squirrel = len(df[df['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(df[df['Primary Fur Color'] == 'Black'])

df_new = pd.DataFrame({
    'Fur Color':['Grey','Cinamon','Black'],
    'Count' : [gray_squirrel,red_squirrel,black_squirrel]
})
print(df.isnull().sum())