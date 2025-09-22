#~~~~~بسم الله الرحمن الرحيم~~~~~#
# Titanic Dataset Analysis and Visualization
#~~~~Importing Libraries~~~~#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#~~~~Setting Plot Style~~~~#
plt.style.use('_mpl-gallery-nogrid') # I'm comfortable with this
#~~~~~Loading Data~~~~~#
train = pd.read_csv('C:\\Users\\AL-ASLY\\Desktop\\My-journey\\titanic\\train.csv')
#~~~~~Data Exploration and Cleaning~~~~~#
# print(train.head(10))
# print(train.shape)
# print(train.dtypes)
# print(train.columns)
print('-'*50)
age = train['Age'].fillna(train['Age'].median()).to_numpy() # Fill missing ages with median age---> To reduce outliers
train['Age'] = age
embarked = train['Embarked'].fillna('S').to_numpy() # Most common embarkation point---> To reduce outliers
train['Embarked'] = embarked
cabin = train['Cabin'].fillna('Missing').to_numpy() # Fill missing cabins with 'Missing'---> You know :D
train['Cabin'] = cabin
fare = train['Fare'].to_numpy()
#~~~~~Statistical Analysis~~~~~#
mean_age = np.mean(age)
mean_fare = np.mean(fare)
std_age = np.std(age , ddof=1)
std_fare = np.std(fare , ddof=1)
median_age = np.median(age)
median_fare = np.median(fare)
stats = pd.DataFrame({
    'Age': [mean_age , std_age , median_age],
    'Fare': [mean_fare , std_fare , median_fare]
}, index=['Mean' , 'Standard Deviation' , 'Median'])
print(stats)
print('-'*50)
#~~~~~Unique Values and Grouped Statistics~~~~~#
print(train['Sex'].unique())
print(train['Embarked'].unique())
print(train['Pclass'].unique())
print('-'*50)
print(train.groupby('Sex')['Survived'].mean()) # Survival
print(train.groupby('Pclass')['Age'].mean()) # Average age by class
print(train.groupby('Embarked')['Fare'].mean()) # Average fare by embarkation point
print('-'*50)
#~~~~~Data Visualization~~~~~#
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
bins = [0,12,18,55,np.inf]
labels = ['Child', 'Teen', 'Adult', 'Senior']
train['AgeGroup'] = pd.cut(train['Age'], bins=bins, labels=labels)
counts = train.groupby(['AgeGroup', 'Sex', 'Pclass']).size().reset_index(name='Count')
pivot = counts.pivot_table(index=['AgeGroup', 'Sex'], columns='Pclass', values='Count', fill_value=0)
pivot.plot(kind='bar', ax=axes[0], stacked=True, title='Counts by Age Group and Sex (stacked by Pclass)', xlabel='Age Group and Sex', ylabel='Count', legend=True,color=['#4c72b0', '#55a868', '#c44e52'],edgecolor='black',width=0.7,grid=True)
axes[0].set_title('Counts by Age Group and Sex')
axes[0].set_xlabel('Age Group and Sex')
axes[0].set_ylabel('Count')
axes[0].legend(title='Pclass')
axes[0].grid(axis='y')
death = train[train['Survived'] == 0]
death_counts = death.groupby(['Sex', 'AgeGroup', 'Pclass']).size().reset_index(name='Count')
death_pivot = death_counts.pivot_table(index=['Sex', 'AgeGroup'], columns='Pclass', values='Count', fill_value=0)
death_pivot.plot(kind='bar', ax=axes[1], stacked=True,color=['#4c72b0', '#55a868', '#c44e52'],edgecolor='black')
axes[1].set_title('Counts of deaths by Sex, Age Group, and Pclass')
axes[1].set_xlabel('Sex and Age Group')
axes[1].set_ylabel('Count')
axes[1].legend(title='Pclass')
axes[1].grid(axis='y')
plt.tight_layout()
plt.show()
