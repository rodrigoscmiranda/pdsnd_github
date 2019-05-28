import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:/Users/TATIL201/Desktop/RODRIGO/UDACITY-PYTHON_PROGRAMMING/chicago.csv',
              'new york city': 'C:/Users/TATIL201/Desktop/RODRIGO/UDACITY-PYTHON_PROGRAMMING/new_york_city.csv',
              'washington': 'C:/Users/TATIL201/Desktop/RODRIGO/UDACITY-PYTHON_PROGRAMMING/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    ways_of_saying = ["chicago", "new york city","new york", "ny", "washington", "washington dc"]
    count_to_validate = 0
    while count_to_validate < 1:
        city = input("Which city do you want to explore: Chicago, New York City or Washington? \n")
        if city.lower() in ways_of_saying:
            print('Let\'s explore {}\'s bikeshare data!'.format(city).title())
            count_to_validate += 1
            break
        else:
            print("\nChoose a valid city\n")
            count_to_validate = 0



    # TO DO: get user input for month (all, january, february, ... , june)
    print("\n\nLet's define a period to explore!\n")
    print("First, let's start with months\n")
    months_ways = ["all", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    validate_month = 0
    while validate_month < 1:
        month = input("If you want to choose a month to filter, type it's name or type 'all' for no month filter: \n")
        if month.lower() in months_ways:
            print("\nYou chose {} to filter.\n".format(month))
            validate_month += 1
            break
        else:
            print("\nChoose a valid month!\n")
            month = input("If you want to choose a month to filter, type it's name or type 'all' for no month filter: \n")
            validate_month = 0


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("\nNow, let's define the day(s) of the week to explore!\n")
    days_ways = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    validate_day = 0
    while validate_day < 1:
        day = input("If you want to choose a week day, type it's name or type 'all' for no week day filter: \n")
        if day.lower() in days_ways:
            print("\nYou chose {} to filter.".format(day))
            validate_day += 1
            break
        else:
            print("\nChoose a valid day!\n")
            day = input("If you want to choose a week day, type it's name or type 'all' for no week day filter: \n")
            validate_day = 0

    print('-'*40)

    if city[:1] == "c":
        city = "chicago"
    elif city[:1] == "n" or city == "ny":
        city = "new york city"
    else:
        city = "washington"


    return city.lower(), month.lower(), day.lower()






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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]

    return df


def time_status(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df["month"].mode()[0]
    print("The most commom month is :\n", popular_month)

    # TO DO: display the most common day of week
    popular_day = df["day_of_week"].mode()[0]
    print("The most commom day is :\n", popular_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]
    print("The most commom hour is :\n", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_status(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_count = df["Start Station"].value_counts().index[0]
    count_start = df["Start Station"].value_counts().values.tolist()[:1]
    print("The most popular Start Station is:\n", start_station_count)
    print("With a total count of:\n", count_start)


    # TO DO: display most commonly used end station
    end_station_count = df["End Station"].value_counts().index[0]
    count_end = df["End Station"].value_counts().values.tolist()[:1]
    print("\nThe most popular End Station is:\n", end_station_count)
    print("With a total count of:\n", count_end)

    # TO DO: display most frequent combination of start station and end station trip

    most_frequent = df.groupby(["Start Station", "End Station"]).size().sort_values(ascending = False)[:1]
    print("\nThe most frequent combination of Start and End Station and it's occurrence count is:\n", most_frequent)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_sec = df["Trip Duration"].sum()
    travel_time_min = travel_time_sec // 60
    travel_time_min2 = travel_time_sec % 60
    print("Total Trip Duration for this filter is: ", travel_time_sec, "seconds or ", travel_time_min, " minutes and", travel_time_min2, "seconds")

    # TO DO: display mean travel time
    avg_travel_time_sec = df["Trip Duration"].mean()
    avg_travel_min = avg_travel_time_sec // 60
    avg_travel_min2 = avg_travel_time_sec % 60
    print("\nThe Average Trip Duration for this filter is: ", avg_travel_time_sec, "seconds or ", avg_travel_min, " minutes and", avg_travel_min2, "seconds")
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_status(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    col = "Gender"
    if col in df.columns:
        gender_count = df["Gender"].value_counts()
        print("\n", gender_count)
    else:
        print("\nWashington does not have Gender data")


    # TO DO: Display earliest, most recent, and most common year of birth
    col = "Birth Year"
    if col in df.columns:
        earliest_year = df["Birth Year"].min()
        most_rec_year = df["Birth Year"].max()
        most_common = df["Birth Year"].mode()[0]
        print("\nThe earlist year of birth is: \n", earliest_year)
        print("The most recent year of birth is: \n", most_rec_year)
        print("The most common year of birth is: \n", most_common)
    else:
        print("Washington does not have Birth Year data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_status(df)
        station_status(df)
        trip_duration_stats(df)
        user_status(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
