#thia ia jut to test
#Domain – 911 Calls 
#focus – data analysis and visualization overview For this capstone project we will be analyzing 911 call data from Kaggle
#This data is from Montgomery Country in the Pennsylvania State of USA. 911 is the most important social security feature of USA. It is the no., 
# which citizens can call in case of any emergencies such as crime, medical, traffic, fire etc.
#import warnings

#import pandas as pd
#import numpy as np
#warnings.filterwarnings('ignore')

#import matplotlib.pyplot as plt
i#mport seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('911.csv')
df.info()
df.head()
### 5 zip code which have highest call##
df['zip'].value_counts().head(5)

## What are the top 5 townships (twp) for 911 calls?

df['twp'].value_counts().head(5)

##Take a look at the 'title' column, how many unique title codes are there?

df['title'].nunique()

sns.countplot(x = 'Month', data = df, palette='viridis', hue = 'Reason')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
