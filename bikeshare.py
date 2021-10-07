import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']

def get_filters():
	""" Asks user to specify a city, month, and day to analyze.
	Returns:
	(str) city - name of the city to analyze
	(str) month - name of the month to filter by, or "all" to apply no month filter
	(str) day - name of the day of week to filter by, or "all" to apply no day filter
	"""
	while True:
		city = input("Please specify which city you're interested in: Chicago, New York City, or Washington. \n: ").strip().strip("'").lower()
		if city == 'chicago' or city == 'new york city' or city == 'washington':
			break
		else:
			print("That's not a valid city name!")
	while True:
		month = input("Are you interested in analyzing data for a specific month? If so, please enter its full name (e.g. January, February). If not, enter 'all' \n : ").strip().strip("'").lower()
		if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
			break
		else:
			print("That's not a valid month name!")
	while True:
		day = input("Are you interested in analyzing data for a specific day of the week? If so, please enter its full name (e.g. Monday, Tuesday). If not, enter 'all' \n: ").strip().strip("'").lower()
		if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
			break
		else:
			print("That's not a valid entry!")
	print('-'*40)
	return city, month, day
def load_data(city, month, day):
	"""Loads data for the specified city and filters by month and day if applicable.
	Args:
	(str) city - name of the city to analyze
	(str) month - name of the month to filter by, or "all" to apply no month filter
	(str) day - name of the day of week to filter by, or "all" to apply no day filter
	Returns:
	df - Pandas DataFrame containing city data filtered by month and day
	"""
	df = pd.read_csv(CITY_DATA[city])
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['month'] = df['Start Time'].dt.month
	df['weekday'] = df['Start Time'].dt.dayofweek
	df['hour'] = df['Start Time'].dt.hour
	df['Start End Combo'] = df['Start Station'] + " to " + df['End Station']
	months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
	days = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6, 'all':7}
	month_num = int(months.index(month) + 1)
	day_num = int(days[day])
	if month != 'all':
		df = df[df['month'] == month_num]
	if day != 'all':
		df = df[df['weekday'] == day_num]
	return df
def time_stats(df, month, day):
	"""Displays statistics on the most frequent times of travel."""
	# TO DO: display the most common month
	if month == "all":
		pop_month_num = df['month'].mode()[0]
		print("\nThe most common travel month is: ", pop_month_num)
	# TO DO: display the most common day of week
	if day == 'all':
		pop_day_num = df['weekday'].mode()[0]
		print("\nThe most common travel day is: ", pop_day_num)
		# TO DO: display the most common start hour
		pop_hour = df['hour'].mode()[0]
		print("\nThe most frequent start hour is: ", pop_hour)
def station_stats(df):
	"""Displays statistics on the most popular stations and trip."""
	# TO DO: display most commonly used start station
	pop_start_station = df['Start Station'].mode()[0]
	print("\nThe most frequently used start station is: ", pop_start_station)
	# TO DO: display most commonly used end station
	pop_end_station = df['End Station'].mode()[0]
	print("\nThe most frequently used end station is: ", pop_end_station)
	# TO DO: display most frequent combination of start station and end station trip
	pop_route = df['Start End Combo'].mode()[0]
	print("\nThe most frequent travel route is: ", pop_route)

def display_data(df):
	view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n :')
	start_loc = 0
	while start > 0:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
		display_data(df)
        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()