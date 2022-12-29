import pandas as pd
df=pd.read_csv("C:/Users/user704/PycharmProjects/pythonProject/pokemon_data.csv")
'''print(df)
print(df.head(4))
print(df.tail(4))
df_txt=pd.read_csv("C:/Users/user704/PycharmProjects/pythonProject/pokemon_data.txt",delimiter='\t')
print(df_txt.head(5))
df['HP']
print(df.columns)
print(df[['Name','Type 1','HP']])
print(df.iloc[0:4])
for index,row in df.iterrows():
    print(index,row['Name'])
df.loc[df['Type 1']=="Grass"]
print(df.iloc[2,1])
#interchanging
df['Type 1'],df['Type 2']=df['Type 2'],df['Type 1']
print(df.to_string())'''
#groupby
df2=df.groupby('Type 1').sum()
print(df2.to_string())



