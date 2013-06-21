# monthly usage stats

import pandas
import os
from matplotlib import pyplot as plt
plt.ioff()
#import style_sheet as ss

dir = os.path.expanduser('~/hv/txt/spd/')

# which files to load

files = ['screenshot', 'hv', 'jhv']
legends = {"screenshot": 'screenshots (Helioviewer.org)',
           "hv": 'movies (Helioviewer.org)',
           "jhv": 'JPX requests (JHelioviewer)'}

# load in the data to a data frame
d={}
for f in files:
    d[f] = pandas.Series.from_csv(''.join((dir,f,'.txt')))

# Raw numbers
numbers_df = pandas.DataFrame(d)
numbers_total = numbers_df.sum(axis=1)
numbers_df.rename(columns=legends, inplace=True)

plt.figure(1)
numbers_df.plot(lw=5)
plt.ylabel('number')
plt.title('Monthly Usage By Service')


# Percentages
dp = {}
for f in files:
    dp[f] = 100*d[f] / numbers_total
percent_df= pandas.DataFrame(dp)
percent_df.rename(columns=legends, inplace=True)

plt.figure(2)
percent_df.plot(lw=5)
plt.ylabel('percentage')
plt.title('Percentage Monthly Usage By Service')
plt.show()


# make it a nice plot...

