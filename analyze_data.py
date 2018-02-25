import csv
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from collections import OrderedDict

loudness = {} # dict to store stats

with open('dr_database.csv') as data:
	database = csv.DictReader(data)
	for album in database:
		year = album['year']
		DR_avg = int(album['DR_avg'])
		
		if year not in loudness.keys():
			loudness[year] = DR_avg
		else:
			loudness[year] = (loudness[year] + DR_avg) / 2


loudness_over_time = OrderedDict(sorted(loudness.items()))

x = loudness_over_time.keys()
y = loudness_over_time.values()

tick_spacing = 5

fig, ax = plt.subplots(1, 1)
ax.plot(x,y)
#ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()