import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    global month
    global day
    Cities = ['chicago', 'new york city', 'washington']
    Months = ['all', 'january', 'february', 'march', 'april', 'may' , 'june']
    Days   = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    city = input("which city do you like to explore its data chicago, new york city or washington?\n ").lower()
    while city not in Cities:
        city = input("Enter a vaild name please!")


    # TO DO: get user input for month (all, january, february, ... , june)
    fil = input("DO you want to filter the data by month, day, or both?\n ")
    if (fil == "month" or fil == "both"):
         month = input("which month do you like to explore its data january, february, march, april, may , june or all for all month?\n ").lower()
         while month not in Months:
            month = input("Enter a valid name please!")
            
   
   


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if (fil == "day" or fil == "both"):
        day = input("which day do you like to explore its data monday, tuesday, wednesday, thursday, friday, saturday, or all for all days?\n ").lower()
        while day not in Days:
            day = input("Enter a valid name please!")
                   
    
                    
    


    print('-'*40)
    return city, month, day
    


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == "all":
        month_arr = pd.DatetimeIndex(df['Start Time']).month
        counts = np.bincount(month_arr)
        print("the most frequently month is: ", np.argmax(counts))
    else:
        print("choose all to get the most frequently month")
   
              
                        
    


    # TO DO: display the most common day of week
    if day == "all":
        day_arr = pd.DatetimeIndex(df['Start Time']).day
        count = np.bincount(day_arr)
        print("the most frequently day is: ", np.argmax(count)) 
    else:
        print("choose all to get the most frequently day")
                  
        
                  


    # TO DO: display the most common start hour
    hour_arr = pd.DatetimeIndex(df['Start Time']).hour
    Counts = np.bincount(hour_arr)
    print("the most frequently hour is: ", np.argmax(Counts))              


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most frequently existed start station is: ", df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print("the most frequently existed end station is: ", df['End Station'].mode())                


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + df['End Station']
    print("the most frequently existed start and end station is: ", df['Combination Station'].mode())  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total duration time is: ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Average duration time is: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city == "washington":
        print("There is no gender data for that city")
    else:
        print(df['Gender'].value_counts()) 
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == "washington":
        print("There is no birth data for that city")
    else:
        print("the Earliest year of birth is: ", df['Birth Year'].min())
        print("the latest year of birth is: ", df['Birth Year'].max())
        print("the most frequently year of birth is: ", df['Birth Year'].mode())
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    answer = input("Do yu want raw data sample , yes/no ? ")
    while answer == "yes":
        print(df.sample(5))
        answer = input("Do yu want raw data sample again , yes/no ? ")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
