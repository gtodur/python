import seaborn as sns
import matplotlib.pyplot as plt

# using scatter plot
sns.set_style='darkgrid'
flowers_df = sns.load_dataset("iris")

# NOTE - order matters
plt.figure(figsize=(12,6))
plt.title("Sepal - Length v/s Width")
sns.scatterplot(x=flowers_df.sepal_length, 
                y=flowers_df.sepal_width, 
                hue=flowers_df.species,
                s=100)
# Seaborn has built-in support for Pandas data frames. 
# Instead of passing each column as a series, you can provide column names and use the data argument to specify a data frame.
#sns.scatterplot(x="sepal_length", y="sepal_width", data=flowers_df, hue=flowers_df.species, s=100)
plt.show()