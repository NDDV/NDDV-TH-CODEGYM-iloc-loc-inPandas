#%%
import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
df

# %%
tg = df.iloc[3]
tg

# %%
tg = df.iloc[3:8]
tg

# %%
tg = df.iloc[[3,5,7]]
tg

# %%
tg = df.iloc[:,1]
tg

# %%
tg = df.iloc[:,3:8]
tg

# %%
tg = df.iloc[3,8]
tg

# %%
tg = df.iloc[3:5,5:7]
tg

# %%
tg = df.loc[3]
tg

# %%
tg = df.loc[:,'UmName']
tg

# %%
tg = df.loc[:,['UmName','Month']]
tg

# %%
tg = df.loc[3,'Price']
tg

# %%
tg = df.loc[df.Year >= 2019]
tg

# %%
df.replace(5,10,inplace = True)
df.head()

# %%
df.replace(52,'RR',inplace = True)
df.head()

# %%
df['Month'].replace(10,5,inplace = True)
df.head()