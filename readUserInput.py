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