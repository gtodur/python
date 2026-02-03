import seaborn as sns
import matplotlib.pyplot as plt

# scatter plots
#import as pandas dataframe
flowers_df = sns.load_dataset("iris")
print(flowers_df)
#print(flowers_df.species.unique())  # unique values for species are - ['setosa' 'versicolor' 'virginica']

# visualize relationships using line chart
plt.xlabel('Sepal Length')
plt.ylabel('Sepal width')
plt.title("Sepal - Length and width comparision")
plt.legend(['Sepal length', 'Sepal width'])
plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
# drawback - does not accurately represent the relationship between sepal length and width
#plt.show()