import pandas as pd

data = pd.read_csv("D:/Courses/Python Projects/Unicorn Startups Analysis/unicorns till sep 2022.csv")

df = pd.DataFrame(data)
df.rename(columns={'Valuation ($B)': 'Valuation', 'Date Joined': 'Date', 'CityÂ':'City'}, inplace= True)
date = df.Date.str.split('/', expand = True)
df['year'], df['month'], df['day'] = date [2], date[1], date[0]

df.year = pd.to_numeric(df.year)
df.month = pd.to_numeric(df.month)
df.day = pd.to_numeric(df.day)
df['Valuation'] = pd.to_numeric(df['Valuation'].str.replace('$', ''))

investors = df.Investors.str.split(',', expand= True)

merged_col = pd.concat([investors[0],investors[1],investors[2],investors[3]], axis = 0).reset_index(drop = True).dropna().str.strip()

print(merged_col)