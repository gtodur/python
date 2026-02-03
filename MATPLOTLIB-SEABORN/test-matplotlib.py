import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# edit default styles directly by modifying the matplotlib.rcParams dictionary
mpl.rcParams['font.size'] = 14
mpl.rcParams['figure.figsize'] = (12, 4)
mpl.rcParams['figure.facecolor'] = '#00000000'

sns.set_style('whitegrid')

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
#plt.figure(figsize=(12, 6)) # change size of the plotted chart (figure)
plt.plot(yield_apples)
#plt.show()

years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.890, 0.929, 0.931]

#plt.plot(years, yield_apples)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')
#plt.show()

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]

sns.set_style("darkgrid")

plt.plot(years, apples, marker='o', color='blue', linestyle='-', linewidth=2, markersize=3, alpha=0.5, markerfacecolor='black')
#plt.plot(years, oranges, 'marker='o', color='red', linestyle='--', linewidth=2, markersize=4, markerfacecolor='green')
fmt = '[marker][line][color]'   # provide shorthand assignment
plt.plot(years, oranges, 'o--r')
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')
plt.title("Crop Yields in Hubli")
plt.legend(['Apples', 'Oranges'])
#plt.show()