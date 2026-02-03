import pandas as pd
covid_df = pd.read_csv('./PANDAS/italy-covid-daywise.csv')
print(type(covid_df))   # returns <class 'pandas.core.frame.DataFrame'>
print(covid_df)         # prints the data, any missing data is displayed as NaN
print(covid_df.info())    # givess metadata of data
print(covid_df.describe())    # gives statistical information for number data
print(covid_df.columns)     # columns of dataframe as object
print(covid_df.shape)       # size

# A dataframe is a dictionary of lists: 
#   keys are column names, and 
#   values are lists/arrays containing data for the respective columns.

# Pandas format is simliar to this
covid_data_dict = {
    'date':       ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases':  [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
}

# Pandas format is NOT similar to this
covid_data_list = [
    {'date': '2020-08-30', 'new_cases': 1444, 'new_deaths': 1, 'new_tests': 53541},
    {'date': '2020-08-31', 'new_cases': 1365, 'new_deaths': 4, 'new_tests': 42583},
    {'date': '2020-09-01', 'new_cases': 996, 'new_deaths': 6, 'new_tests': 54395},
    {'date': '2020-09-02', 'new_cases': 975, 'new_deaths': 8 },
    {'date': '2020-09-03', 'new_cases': 1326, 'new_deaths': 6},
]

print(covid_df['new_cases'])            # prints all new cases
print(type(covid_df['new_cases']))    # returns <class 'pandas.core.series.Series'>
# SERIES - essentially a numpy array with some extra methods and properties
print(covid_df['new_cases'][6])         # index based access
print(covid_df.at[6, 'new_cases'])      # at a position within a series
print(covid_df.new_cases)               # returns a series of new_cases column

print(covid_df[['date', 'new_deaths']]) # sub-dataframe consisting date and new_deaths columns only
# it is just a view to the original dataframe, any change there will reflect here.

covid_df_copy = covid_df.copy()         # copy, both are separate, change in one does not affect the other

print(covid_df_copy.loc[6])             # displays 7th row entirely, which is also a Series object
print(covid_df_copy.loc[3:6])           # displays 4th to 7th row entirely, which is also a Series object
print(type(covid_df.loc[6]))            # pandas.core.series.Series

print(covid_df_copy.head(2))            # display first 2 rows
print(covid_df_copy.tail(2))            # display last 2 rows
print(covid_df_copy.sample(5))           # returns a sample of 5 rows, preserving their indexes

print(covid_df_copy.new_tests.first_valid_index())  # index within new_tests from which a valid number is present and not NaN

# Questions can be answered by doing mathematics on the data
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
print('The number of reported cases is {} and the number of reported deaths is {}.'.format(int(total_cases), int(total_deaths)))

death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()
print("The overall reported death rate in Italy is {:.2f} %.".format(death_rate*100))

# filter
high_new_cases = covid_df.new_cases > 2500    
print(high_new_cases)                           # gives out all rows, but true/false depending on criteria satisfied
print(covid_df[high_new_cases])                 # gives out only rows which had true in the high_new_cases 

# high positive rate records
positive_rate = 0.05206657403227681
high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]   # df[...]   returns filtered rows as per the calculation
print(high_ratio_df)

# The result of performing an operation on two columns is a new series.
covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests
print(covid_df)
# after dropping column
covid_df.drop(columns=['positive_rate'], inplace=True)  
# with inplace=True, existing dataframe is itself affected, so can print that
# without inplace, need to set to assign to a new dataframe 
print(covid_df)

# sort rows
sorted_covid_df = covid_df.sort_values('new_cases', ascending=False).head(3)
print(sorted_covid_df)

# if one of the Series value is incorrect, like a negative number
# then we can either - 
#   Replace it with 0.
#   Replace it with the average of the entire column
#   Replace it with the average of the values on the previous and next date
#   Discard the row entirely

# substitute with average of nearby values
covid_df.at[3, 'new_tests'] = (covid_df.at[2, 'new_tests'] + covid_df.at[4, 'new_tests'])/2
print(covid_df)

# working with dates
covid_df['date'] = pd.to_datetime(covid_df.date)
print(covid_df['date'])

covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

print(covid_df)

# Query the rows for June
covid_df_june = covid_df[covid_df.month == 6]

# Extract the subset of columns to be aggregated
covid_df_june_metrics = covid_df_june[['new_cases', 'new_deaths', 'new_tests']]

# Get the column-wise sum
covid_june_totals = covid_df_june_metrics.sum()

print(covid_june_totals)            # get totals of each

# combine everything into one
print(covid_df[covid_df.month == 6][['new_cases', 'new_deaths', 'new_tests']].sum())

print(type(covid_june_totals))     # pandas.core.series.Series

print(covid_june_totals['new_cases'])   # get total of new_cases only


# group and aggregate data
covid_month_wise_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
print(covid_month_wise_df)

covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()
print(covid_month_mean_df)

covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + 1000
# while cumsum(), NaN values are unaffected
print(covid_df)

# Merge Data from Multiple Sources
import urllib.request
urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

locations_df = pd.read_csv('locations.csv')
print(locations_df)
print(locations_df[locations_df.location == "Italy"])
covid_df['location'] = "Italy"  # insert new column because while merging we need to have at least 1 column common between 2 dataframes
merged_df = covid_df.merge(locations_df, on="location") # merge 2 dataframes
print(merged_df)

# now can calculate cases per million
merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population
print(merged_df)    # now has data per million as computed above


# Write Data Back to Files
result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]
result_df.to_csv('./PANDAS/merged-results.csv', index=None)

# Chart plotting in Pandas
#import matplotlib.pyplot as plt
#merged_df.new_cases.plot(title="New cases", kind='line', x='date', y='new_cases', xlabel='Month', ylabel='Cases', figsize=(8, 5), legend=True)
#merged_df.new_deaths.plot()
#plt.show()