# monthly usage stats

import pandas
import os
#import style_sheet as ss

dir = os.path.expanduser('~/hv/txt')

# which files to load

files = ['screenshot', 'hv', 'jhv']

# load in the data to a data frame
d={}
for f in files:
    d[f] = pandas.Series.from_csv(''.join(dir,f,'.txt'))

df = pandas.DataFrame(d)

# make it a nice plot...

