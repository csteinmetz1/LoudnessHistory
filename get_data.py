from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
import pandas as pd

# total number of pages to scrape
total_pages = 1181 # as of 2/13/2018

# dict to store columns
database = OrderedDict({'artist' : [], 
						'album' : [],
						'year' : [],
						'DR_avg' : [],
						'DR_min' : [],
						'DR_max' : [],
						'codec' : [],
						'source' : []})

# iterate over each page
for page_number in range(1,total_pages+1):
	page = requests.get('http://dr.loudness-war.info/album/list/'+str(page_number))
	soup = BeautifulSoup(page.text, 'html.parser')

	# only grab the second table, it has the info we want
	tables = soup.find('body').find_all('table')
	album_table = tables[1]

	data = album_table.find_all('tr')

	for entry in data:
		if len(entry.find_all('td')) != 0:
			try:
				database['artist'].append(entry.find_all('td')[0].text)
				database['album'].append(entry.find_all('td')[1].a.text)
				database['year'].append(entry.find_all('td')[2].text)
				database['DR_avg'].append(entry.find_all('td')[3].text)
				database['DR_min'].append(entry.find_all('td')[4].text)
				database['DR_max'].append(entry.find_all('td')[5].text)
				database['codec'].append(entry.find_all('td')[6].text)
				database['source'].append(entry.find_all('td')[7].text)
			except:
				print('No entries found.')
	
	print("Got", page_number, "pages.", total_pages-page_number, "pages remain.")

# create dataframe and save result to csv
dataframe = pd.DataFrame(database)
print(dataframe.head())
dataframe.to_csv("dr_database.csv", sep=',')

	

