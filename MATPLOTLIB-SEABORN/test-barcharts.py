import matplotlib.pyplot as plt
import seaborn as sns

# years = range(2000, 2006)
# apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
# oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

# plt.bar(years, oranges)
# plt.bar(years, apples, bottom=oranges)
# plt.show()

# --------------------------------------------------------

# Bar Plots with Averages in Seaborn

#tips_df = sns.load_dataset("tips")

# sns.barplot(x='day', y='total_bill', data=tips_df)
# sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df)   # total bill for male & females
# The lines cutting each bar represent the amount of variation in the values

#You can make the bars horizontal simply by switching the axes.
#sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df)


#plt.show()

# --------------------------------------------------------

# Heat maps with Seaborn
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df)

# display the actual values in each block
#sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues')

plt.show()