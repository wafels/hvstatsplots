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


f = 'Analytics www.helioviewer.org Audience Overview 20110201-20130621.csv'

# load in the data to a data frame
d = pandas.Series.from_csv(''.join((dir, f)))

plt.figure(1)
plt.xlabel('daily number of visits')
plt.ylabel('number of occurrences')
plt.title('frequency distribution of Helioviewer.org daily visits')
d.hist(bins=40)
plt.annotate(str(d.sum())+' visits', xy=(0.55,0.7), textcoords='figure fraction')
plt.annotate(str(d.index[0].date()) + ' - '+ str(d.index[-1].date()), xy=(0.55,0.75), textcoords='figure fraction')
plt.savefig(''.join((img,'daily_hist','.',format)), format=format)


plt.figure(2)
plt.ylabel('number of visits')
plt.title('Helioviewer.org daily visits')
ann = d.index[100]
plt.annotate(str(d.sum())+' visits', xy=(ann,14000))
plt.annotate(str(d.index[0].date()) + ' - '+ str(d.index[-1].date()), xy=(ann,15000))
d.plot(lw=1)
plt.savefig(''.join((img,'daily_ts','.',format)), format=format)

