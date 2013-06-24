# files per observatory instrument detector measurement

import pandas
import os 
from matplotlib import pyplot as plt
import style_sheet as ss

plt.ioff()

dir = ss.data_directory
img = ss.image_directory
format = ss.format

# which files to load


f = 'datasources.csv'

# load in the data to a data frame
df = pandas.DataFrame.from_csv(''.join((dir, f)))

# Need to create a new index from the observatory-instrument-detector columns
# also get the number of files out


# This new data frame now is now the one we need to plot, using a bar plot


df["Visits"].plot(kind='bar', color='red')
plt.ylabel('Number of visits')
plt.title('Top 10 countries/territories by number of visits')
plt.annotate(str(df["Visits"].sum())+' visits', xy=(0.55,0.7), textcoords='figure fraction')
plt.annotate('up to  2013-06-24', xy=(0.55,0.75), textcoords='figure fraction')
plt.savefig(''.join((img,'hvfiles','.',format)), format=format, bbox_inches='tight')
