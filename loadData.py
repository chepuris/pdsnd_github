import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


df = pd.read_csv(CITY_DATA.get('chicago'))

# extract day of week from the Start Time column 
df['Day_of_Week'] = pd.to_datetime(df['Start Time']).dt.weekday_name

# extract month from the Start Time column
df['Month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')

# extract hour from the Start Time column
df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour

# make a copy
df2 = df.copy()
print(df2.shape)

# display most common month
most_common_month = df2['Month'].value_counts().idxmax()
max_count = df2['Month'].value_counts().max()
print('Most popular Month is {} and rented for {} times in the month of {}.'.format(most_common_month, max_count, most_common_month))

# display most common day of week
most_common_day = df['Day_of_Week'].value_counts().idxmax()
max_count = df['Day_of_Week'].value_counts().max()
print('Most popular Day of week is {} and rented for {} times on {}.'.format(most_common_day, max_count, most_common_day + 's'))

# display most common start hour
most_common_hour = df['Hour'].value_counts().idxmax()
max_count = df['Hour'].value_counts().max()
print('Most popular Hour is {} and rented for {} times during this {}.'.format(most_common_hour, max_count, most_common_hour))


# filter by month
df = df[df['Month']=='June'] 

# filter by day of week
df = df[df['Day_of_Week']=='Friday']

print(df.shape)
print(df.head(20))

# total and average trip duration
total_trip_duration = df['Trip Duration'].sum()
print("Total trip duration is {} min". format(total_trip_duration // 60))

# average trip duration 
print("Average trip duration is {} min.".format(df['Trip Duration'].mean() // 60))

# total bike rentals for the selected city, month, day of week
print('There are total {} bike rentals for the selected city, month, day of week'.format(len(df.index)))

# most popular start station
popular_start_station = df['Start Station'].value_counts().idxmax()
max_count = df['Start Station'].value_counts().max()
print('Most popular start station is {} and bikes rented for {} times from here.'.format(popular_start_station, max_count))

# most popular end station
popular_end_station = df['End Station'].value_counts().idxmax()
max_count = df['End Station'].value_counts().max()
print('Most popular End station is {} and bikes rented for {} times from here.'.format(popular_end_station, max_count))

# most popular trips between stations
# df = df.groupby(by=['Start Station', 'End Station'])
# print(df['Start Station', 'End Station'].head(10))

# counts of user types
user_types = df['User Type'].value_counts()
print(user_types)

# check condition for city is chicago or new york city
# Display counts of gender
gender = df['Gender'].value_counts()
print(gender)

# Display counts of NaN in gender
count = df['Gender'].isnull().sum().sum()
print('{} have no gender available.'.format(count))

# display earliest, recent, common year of birth
earliest_year = df['Birth Year'].min()
print('Earliest Birth year {}'.format(earliest_year))

recent_year = df['Birth Year'].max()
print('Recent Birth year {}'.format(recent_year))

# most popular birth year
popular_birth_year = df['Birth Year'].value_counts().idxmax()
max_count = df['Birth Year'].value_counts().max()
print('Most popular birth year is {} and rented for {} times.'.format(popular_birth_year, max_count))





