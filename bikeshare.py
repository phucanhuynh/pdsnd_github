
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    city_input = True
    city = ''
    while city_input:
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
        if city in ('chicago','new york','washington'):
            city_input = False
            break
        else:
            print('Please check your input')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = True
    month = ''
    while month_input:
        print('Would you like to filter the data by month, day, or not at all?\n')
        month = input('Please choose month filter: January, February, March, April, May, June, All: ').lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            month_input = False
            break
        else:
            print('Please check your input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input = True
    day = ''
    while day_input:
        day = input('Please choose day filter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All: ').lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            day_input = False
            break
        else:
            print('Please check your input')

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
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    # this column is used for further function after this
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week:', common_day)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The commonly used end station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'].str.cat(df['End Station'], sep='-')
    common_combi_station = df['Combined Station'].mode()[0]
    print('The most frequent combination of start station and end station trip:', common_combi_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time:', travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    #provide time to calculate duration at the end
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of user types: ',df['User Type'].value_counts())

    # No display gender and year of birth if they don't exist
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('Count of gender: ',df['Gender'].value_counts())
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

# TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest year of birth: ', df['Birth Year'].min())
        print('Most recent year of birth: ', df['Birth Year'].max())
        print('Most common year of birth: ', df['Birth Year'].mode()[0])
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_display_row(df):
    """Displays statistics 5 rows when asked"""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ").lower()
    if view_data == 'yes':
        print(df.iloc[1:5])
        start_loc = 5
        end_loc = 10
        view_display = input("Do you wish to continue? Enter yes or no? ").lower()
        while view_display == 'yes':
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5
            view_display = input("Do you wish to continue? Enter yes or no? ").lower()
            if view_display == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_display_row(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
