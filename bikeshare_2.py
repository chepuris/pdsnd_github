import time
import pandas as pd
import numpy as np

CITY_DATA = { 1: ['chicago', 'chicago.csv'],
                2: ['new york city', 'new_york_city.csv'],
                3: ['washington','washington.csv'] } 
# this function is implemented to interpret user raw input on city, month and day 
def get_filters_updated():
    print('\nHello! Let\'s explore some US bikeshare data. Which city data would you be interested.\n\n Enter your choice of city, Chicago, New York City, Washington.\n\n')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city_list = ['chicago', 'washington', 'new york city']
    city_dict = { 'chicago':'chicago.csv',
                'new york city':'new_york_city.csv',
                'washington':'washington.csv' }
    while True:
        try:
            city_name = (input("Provide your choice of city here:"))
            if city_name.lower() in city_dict.keys():
                city = city_name.lower()
                fileName = city_dict[city]
                print(fileName)
                print('\nThanks, we will explore bikeshare data for \033[1m {} \033[0m.'.format(city.title()))
                break
            else:
                print('That\'s not a valid value for the available city data. Please choose from Chicago, New York City, Washington.')    
        except:
            print('That\'s not a valid value for the available city data. Please choose from Chicago, New York City, Washington.')    
        finally:
            pass

    # get user input for month (all, january, february, ... , june)
    print('-'*40)

    print('\nFor the selected city, which month of year would you be interested to analyze. Enter name of the month, enter "All" to apply no month filter.')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    MONTH_DATA = { 'All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}
    while True:
        try:
            month_name = (input("Provide your choice of month here:"))
            if month_name.lower().title() in MONTH_DATA:
                month = month_name.lower().title()
                print(month)
                print('\nThanks, we will explore bikeshare data for \033[1m {} \033[0m.'.format(month))
                break
            else:
                print('That\'s not a valid value for the month filter. Please choose from all, January, February, March, April, May, June, July, August, September, October, November, December')    
        except:
            print('That\'s not a valid value for the month filter. Please choose from all, January, February, March, April, May, June, July, August, September, October, November, December')    
        finally:
            pass

    # get user input for month (all, january, february, ... , june)
    print('-'*40)

    print('For the selected city and month of year filter would you be interested to analyze data by day of the week. Enter 0 to apply no day filter.')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    WEEK_DAY = { 'All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
    while True:
        try:
            day_name = (input("Provide your choice of day of week here:"))
            if day_name.lower().title() in WEEK_DAY:
                day = day_name.lower().title()
                print(day)
                print('\nThanks, we will explore bikeshare data for \033[1m {} \033[0m.'.format(day))
                break
            else:
                print('That\'s not a valid value for the day of the week filter. Please choose from All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday')    
        except:
            print('That\'s not a valid value for the day of the week filter. Please choose from All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday')
        finally:
            pass

    # get user input for month (all, january, february, ... , june)
    print('-'*40)
    return city, fileName, month, day

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    MONTH_DATA = { 0:'all, no month filter applied', 1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    DAY_WEEK_DATA = {0:'all, no day filter applied', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

    print('Hello! Let\'s explore some US bikeshare data. Which city data would you be interested.\n\n Enter 1 for Chicago, \n Enter 2 for New York City, \n Enter 3 for Washington.\n\n')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_name = int(input("Provide your input here:"))
            city = CITY_DATA.get(city_name)[0]
            fileName = CITY_DATA.get(city_name)[1]
            #print(fileName)
            print('\nThanks, we will explore bikeshare data for \033[1m {} \033[0m.'.format(city.title()))
            break
        except:
            print('That\'s not a valid value for the available city data. Please choose from the available choices 1 or 2 or 3.')
        finally:
            pass

        # get user input for month (all, january, february, ... , june)
    print('-'*40)

    print('For the selected city, which month of year would you be interested to analyze. Enter 0 to apply no month filter.')
    for key in MONTH_DATA:
        print('Enter {} for {}'.format(key, MONTH_DATA[key]))

    while True:
        try:
            month_name = int(input("\nProvide your input here:"))
            if month_name in MONTH_DATA and month_name != 0:
                month = MONTH_DATA.get(month_name)
                print('\nThanks, we will explore bikeshare data for the month of \033[1m {} \033[0m.'.format(month))
                break
            elif month_name in MONTH_DATA and month_name == 0:
                month = 'all'
                print('\nThanks, no month filter will be applied.')
                break
            else:
                print('That\'s not a valid value for the month. Please choose from the available choices 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12.')        
        except:
            print('That\'s not a valid value for the month. Please choose from the available choices 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12.')
        finally:
            pass
    print('_'*40)
        # get user input for day of week (all, monday, tuesday, ... sunday)

    print('For the selected city and month of year filter would you be interested to analyze data by day of the week. Enter 0 to apply no day filter.')
    for key in DAY_WEEK_DATA:
        print('Enter {} for {}'.format(key, DAY_WEEK_DATA[key]))

    while True:
        try:
            day_name = int(input("\nProvide your input here:"))
            if day_name in DAY_WEEK_DATA and day_name != 0:
                day = DAY_WEEK_DATA.get(day_name)
                print('\nThanks, we will explore bikeshare data for the month of \033[1m {} \033[0m.'.format(day))
                break
            elif day_name in DAY_WEEK_DATA and day_name == 0:
                day = 'all'
                print('\nThanks, no day filter will be applied.')
                break
            else:
                print('That\'s not a valid value for the day of the week. Please choose from the available choices 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7.')        
        except:
            print('That\'s not a valid value for the day of the week. Please choose from the available choices 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7.')
        finally:
            pass

        print('-'*40)
    return city, fileName, month, day


def load_data(city, fileName, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #df = pd.read_csv('/Users/teeshan/Desktop/ND/scripts/bikeshare/bikeshare-2/'+fileName)
    df = pd.read_csv(fileName)

    # extract day of week from the Start Time column 
    df['Day_of_Week'] = pd.to_datetime(df['Start Time']).dt.weekday_name

    # extract month from the Start Time column
    df['Month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')

    # extract hour from the Start Time column
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour

    print(df.shape)
    print(df.head(5))

    # filter by month
    if month.lower() == 'all':
        pass
    else:
        df = df[df['Month']==month] 

    # filter by day of week
    if day.lower() == 'all':
        pass
    else:
        df = df[df['Day_of_Week']==day]
    print('After filter') 
    print(df.shape)
    print(df.head(5))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # display most common month
    most_common_month = df['Month'].value_counts().idxmax()
    max_count = df['Month'].value_counts().max()
    print('Most popular Month is {} and rented for {} times in the month of {}.'.format(most_common_month, max_count, most_common_month))

    # display most common day of week
    most_common_day = df['Day_of_Week'].value_counts().idxmax()
    max_count = df['Day_of_Week'].value_counts().max()
    print('Most popular Day of week is {} and rented for {} times on {}.'.format(most_common_day, max_count, most_common_day + 's'))

    # display most common start hour
    most_common_hour = df['Hour'].value_counts().idxmax()
    max_count = df['Hour'].value_counts().max()
    print('Most popular Hour is {} and rented for {} times during this {} +th hour.'.format(most_common_hour, max_count, most_common_hour))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
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

    # display most frequent combination of start station and end station trip    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    # total and average trip duration
    total_trip_duration = df['Trip Duration'].sum()
    print("Total trip duration is {} min". format(total_trip_duration // 60))

    # average trip duration 
    print("Average trip duration is {} min.".format(df['Trip Duration'].mean() // 60))

    # total bike rentals for the selected city, month, day of week
    print('There are total {} bike rentals for the selected city, month, day of week'.format(len(df.index)))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    # counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if city == 'chicago' or city == 'new york city':
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
    else:
        print('No data available for selected city.')
    print('-'*40)


def main():
    while True:
        city, fileName, month, day = get_filters_updated()
        #city, month, day = 'chicago', 'June', 'Friday'
        
        print(city)
        print(fileName)
        print(month)
        print(day)
        STATS = {1:'Time Stats', 2:'Station Stats', 3:'Trip Duration Stats', 4:'User Stats', 5:'Display first few rows of raw data', 6:'Restart Program', 7:'Exit Program'}
        
        df = load_data(city, fileName, month, day)
        if df.empty == True:
            restart = input('\nSelected choices resulted in zero results, would you like to restart? Enter yes or no.\n')
        else:
            pass
        
        while True and df.empty == False:
            try:
                print("\nFor the selected city and month, day filter criteria. What stats would you like to see.")
                for key in STATS:
                    print('Enter {} for {}'.format(key, STATS[key]))
                user_sel = int(input("\nProvide your input here:"))
                if user_sel in STATS:
                    if user_sel == 1:
                        time_stats(df)
                    elif user_sel == 2:
                        station_stats(df)
                    elif user_sel == 3:
                        trip_duration_stats(df)
                    elif user_sel == 4:
                        user_stats(df, city)
                    elif user_sel == 5:
                        print('First few rows of dataframe:')
                        print('-'*40)
                        print(df.head(5))
                    elif user_sel == 6:
                        restart = 'yes'
                        break
                    elif user_sel == 7:
                        restart = 'no'
                        break
                    else:
                        pass
                else:
                    print('\n\nThat\'s not a valid value to display stats. Please choose from the available choices 1 or 2 or 3 or 4 or 5 or 6 or 7.') 
            except:
                print('\n\nThat\'s not a valid value to display stats. Please choose from the available choices 1 or 2 or 3 or 4 or 5 or 6 or 7.') 
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
