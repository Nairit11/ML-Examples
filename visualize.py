#Import required libraries
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sns

#Read data
df = pd.read_csv('F:\Pokemon.csv', index_col=0)

#To plot a scatter plot
sns.lmplot(x='Attack', y='Defense', data=df)
#Can also be written as sns.lmplot(x=df.attack,y=df.Defense)

#Customize using seaborn and matplotlib
sns.lmplot(x='Attack', y='Defense', data=df, fit_reg=False, hue='Stage')
plt.xlim(0,None)
plt.ylim(0,None)

#Box plot only the stats
stats_df=df.drop(['Total', 'Stage', 'Legendary'], axis=1)
sns.boxplot(data=stats_df)

