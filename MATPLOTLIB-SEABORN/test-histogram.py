import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")

#plt.title("Distribution of Sepal Width")
#plt.hist(flowers_df.sepal_width)    # display all bins

# Specifying the number of bins
#plt.hist(flowers_df.sepal_width, bins=4)

# Specifying the boundaries of each bin
#plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))


#plt.show()

# --------------------------------------------------------------------

# Multiple Histograms
# setosa_df = flowers_df[flowers_df.species == 'setosa']
# versicolor_df = flowers_df[flowers_df.species == 'versicolor']
# virginica_df = flowers_df[flowers_df.species == 'virginica']

# plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
# plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))

# plt.show()

# --------------------------------------------------------------------

# We can also stack multiple histograms on top of one another.

plt.title('Distribution of Sepal Width')
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica'])
plt.show()
