# monthly usage stats

import pandas
import os
from matplotlib import pyplot as plt
import style_sheet as ss

plt.ioff()

dir = ss.data_directory
img = ss.image_directory
format = ss.format

# which files to load

files = ['screenshot', 'hv', 'jhv']
nlegends = {"screenshot": '# screenshots (Helioviewer.org)',
           "hv": '# movies (Helioviewer.org)',
           "jhv": '# JPX requests (JHelioviewer)'}

plegends = {"screenshot": '% screenshots (Helioviewer.org)',
           "hv": '% movies (Helioviewer.org)',
           "jhv": '% JPX requests (JHelioviewer)'}

# load in the data to a data frame
d={}
for f in files:
    d[f] = pandas.Series.from_csv(''.join((dir,f,'.txt')))

# Raw numbers
numbers_df = pandas.DataFrame(d)
numbers_total = numbers_df.sum(axis=1)
numbers_df.rename(columns=nlegends, inplace=True)

plt.figure(1, figsize=(20, 6))
numbers_df.plot(lw=5, logy=True)
plt.ylabel('number')
plt.title('Monthly Usage By Service')
plt.legend(fontsize=10, loc=2)
plt.savefig(''.join((img,'monthly_number','.',format)), format=format)

# Percentages
dp = {}
for f in files:
    dp[f] = 100*d[f] / numbers_total
percent_df= pandas.DataFrame(dp)
percent_df.rename(columns=plegends, inplace=True)

plt.figure(2)
percent_df.plot(lw=5)
plt.ylabel('percentage (%)')
plt.title('Percentage Monthly Usage By Service')
plt.legend(fontsize=10, loc=7)
plt.savefig(''.join((img,'monthly_percent','.', format)), format=format)

"""
full = numbers_df.join(percent_df)
plt.figure()
ax = full.plot(lw=5, secondary_y=['% screenshots (Helioviewer.org)', '% movies (Helioviewer.org)', '% JPX requests (JHelioviewer)'  ])
ax.set_ylabel('percentage (%)')
ax.right_ax.set_ylabel('number')
plt.show()
# make it a nice plot...
"""
