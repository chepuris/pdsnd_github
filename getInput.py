"""
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
CITY_DATA = { 1: ['chicago', 'chicago.csv'],
              2: ['new york city', 'new_york_city.csv'],
              3: ['washington','washington.csv'] } 
MONTH_DATA = { 0:'all, no month filter applied', 1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
DAY_WEEK_DATA = {0:'all, no day filter applied', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

print('Hello! Let\'s explore some US bikeshare data. Which city data would you be interested.\n\n Enter 1 for Chicago, \n Enter 2 for Washington, \n Enter 3 for New York City.\n\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
while True:
    try:
        city_name = int(input("Provide your input here:"))
        city = CITY_DATA.get(city_name)[0]
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