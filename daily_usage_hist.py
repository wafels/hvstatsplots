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
f = 'api_daily.csv'

# data frame
df = pandas.DataFrame.from_csv(''.join((dir,f)), header=None, index_col = 1)

# Get the unique indices
#services = df.X0.unique()
all_services = ['buildMovie', 'embed', 'getClosestImage', 'getJPX',
                'takeScreenshot', 'uploadMovieToYouTube']

# go through each and get each
all={}
for service in all_services:
    s = df[df.X0==service]["X2"]
    s.name = service
    all[service] = s

numbers_df = pandas.DataFrame(all)


#files = ['screenshot', 'hv', 'jhv']
nlegends = {"takeScreenshot": '# screenshots (Helioviewer.org)',
           "buildMovie": '# movies (Helioviewer.org)',
           "getJPX": '# JPX requests (JHelioviewer)',
           "embed": "# embedded (Helioviewer.org)",
           "getClosestImage": "# get closest image (Helioviewer.org)",
           "uploadMovieToYouTube": "# upload movie to YouTube from Helioviewer.org"}

colors ={"# screenshots (Helioviewer.org)": 'm',
           "# movies (Helioviewer.org)": 'b',
           "# JPX requests (JHelioviewer)": 'c',
           "# embedded (Helioviewer.org)": "g",
           "# get closest image (Helioviewer.org)": "r",
           "# upload movie to YouTube from Helioviewer.org": "y"}
"""
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
"""

legend_fontsize = 8 

# load in the data to a data frame
#d={}
#for f in files: 
#    d[f] = pandas.Series.from_csv(''.join((dir,f,'.txt')))

# Raw numbers
#numbers_df = pandas.DataFrame(d)
numbers_total = numbers_df.sum(axis=1)
numbers_df.rename(columns=nlegends, inplace=True)

for index, service in enumerate(nlegends.values()):
    fig = plt.figure(index)
    numbers_df[service].hist(bins=50, color=colors[service])
    plt.ylabel('number of occurences')
    plt.xlabel('number of daily service requests')
    plt.title(service)
#leg = plt.legend(fontsize=legend_fontsize, loc=2, fancybox=True)
#leg.get_frame().set_alpha(0.5)
#plt.annotate(str(numbers_df.index[0].date()) + ' to '+ str(numbers_df.index[-1].date()), xy=(numbers_df.index[1],200))
    plt.savefig(''.join((img,'daily_usage_h',service,'.',format)), format=format, dpi=200)




"""
# Percentages
pc_services = ['buildMovie', 'embed', 'getJPX',
                'takeScreenshot', 'uploadMovieToYouTube']
dp = {}
for f in all_services:
    dp[f] = 100*[f] / numbers_total
percent_df= pandas.DataFrame(dp)
percent_df.rename(columns=plegends, inplace=True)

plt.figure(2)
percent_df.plot(lw=5)
plt.ylabel('percentage (%)')
plt.title('Percentage Monthly Usage By Service')
plt.legend(fontsize=10, loc=7)
plt.savefig(''.join((img,'monthly_percent','.', format)), format=format)

full = numbers_df.join(percent_df)
plt.figure()
ax = full.plot(lw=5, secondary_y=['% screenshots (Helioviewer.org)', '% movies (Helioviewer.org)', '% JPX requests (JHelioviewer)'  ])
ax.set_ylabel('percentage (%)')
ax.right_ax.set_ylabel('number')
plt.show()
# make it a nice plot...
"""