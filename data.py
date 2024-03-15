import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('TWO_CENTURIES_OF_UM_RACES.csv')

#see the data thats been imported 

# info =df.info()


#clean up data
# only want usa races , 50k  or 50 mi , 2020

k = df[df['Event distance/length'] == '50km']
k = df[df['Event distance/length'] == '50mi']


#combine 50k/50mi with isin

k = df[df['Event distance/length'].isin(['50km','50mi'])]
k = df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020 ) ]
k = df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']

#combine  all the filters together 

k = df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020 ) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]

df2 = df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020 ) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


#remove (USA) from event name 

k = df2['Event name'].str.split('(').str.get(0)

#clean  up athlete age 

k = df2['athlete_age'] = 2020 - df2['Athlete year of birth']

#remove h from athlete performance 

k = df2['Athlete performance'].str.split(' ').str.get(0)

#drop columns : athlete club, athlete country  , athlete  year of birth , athlete age category

df2 = df2.drop(['Athlete club', 'Athlete country', 'Athlete year of birth', 'Athlete age category'], axis=1)

#clean up  null values

df2.isna().sum

df2 = df2.dropna()

#check for dupes

k = df2[df2.duplicated()==True]


#reset index 

k = df2.reset_index(drop=True)
print(k)

#fix types

df2.dtypes

df2['athlete_age'] = df2['athlete_age'].astype(int)

df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)

# rename columns

#  0   Year of event              int64
#  1   Event dates                object
#  2   Event name                 object
#  3   Event distance/length      object
#  4   Event number of finishers  int64
#  5   Athlete performance        object
#  6   Athlete club               object
#  7   Athlete country            object
#  8   Athlete year of birth      float64
#  9   Athlete gender             object
#  10  Athlete age category       object
#  11  Athlete average speed      object
#  12  Athlete ID                 int64

df2 = df2.rename(columns={'Year of event': 'year' ,
                          'Event dates': 'race_day',
                          'Event name': 'race_name',
                          'Event distance/length': 'race_length',
                          'Event number of finishers': 'race_number_of_finishers',
                          'Athlete performance': 'athlete_performance',
                          'Athlete gender': 'athlete_gender',
                          'Athlete average speed': 'athlete_average_speed',
                          'Athlete ID': 'athlete_id',
})

#reorder columns

df3 = df3 = df2[['race_day', 'race_name', 'race_length', 'race_number_of_finishers','athlete_performance', 'athlete_gender', 'athlete_average_speed', 'athlete_id']]

df3.head()

#charts and graphs

sns.histplot(df3['race_lenght'])

sns.histplot(df3, x = 'race_lenght', hue ='athlete_gender' )

sns.lmplot(data=df3, x='athlete_age', y= 'athlete_average_speed')




