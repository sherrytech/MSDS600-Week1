# Lines starting with # are comments and are not run by Python.
"""
Multi-line comments are possible with triple quotes like this.
"""
# pandas is a common library for working with data in Python, we usually import it like so:
import pandas as pd
import matplotlib.pyplot as plt

# This data comes from the UCI ML repository:
# https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset
# It is the daily number of users from a bike share program
df = pd.read_csv('day.csv')

df.head()
df.describe()

# Use the examples in the jupyter notebook to help you here.
# calculate the mean and standard deviation of the hourly data counts (the 'cnt' column)
# mean
a=df.cnt.mean()
print("Mean = "+str(a))
# standard deviation
print("Standard deviation = "+ str(df.cnt.std()))

# plot the counts ('cnt' column)
fig, ax = plt.subplots()

plt.plot(df.dteday, df.cnt)

# display x ticks for every 150th label to avoid overlapping
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % 150 != 0: label.set_visible(False)

plt.xlabel('Date')            # lable x axis
plt.ylabel("Daily Users Count")  # lable y axis
plt.title('Bike Share Dataset')  # title the plot
plt.show()                       # show the plot