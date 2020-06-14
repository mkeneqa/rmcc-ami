import fire
import requests
from bs4 import BeautifulSoup
import time
import sys
import re
import datetime
from tinydb import TinyDB, Query

def crawl_archive():
	db = TinyDB('db.json',sort_keys=True, indent=4, separators=(',', ': '))
	db.drop_tables()
	print("clearing tables...")
	series_table = db.table('series')
	episode_table = db.table('episode')


	base_url = "https://messages.calvarychapel.ca"

	print("scraping {} ...".format(base_url))
	
	for n in range(1,300):

		result = requests.get('{}/?series={}'.format(base_url,n))
		res_content = result.content

		soup = BeautifulSoup(res_content,'html.parser' )
		section = soup.find(id='lblSection').text
		title = soup.find(id='rptSeries_lblSeries_0').text
		book = soup.find(id='lblBook').text
		
		if title is not None:
			series = {
				'series_id': n,
				'category': section,
				'label': book,
				'title': title
			}
			
			table_rows = soup.find("table",{"class":"table rmcc-table"}).find("tbody").find_all("tr")
			for row in table_rows:
				episode_date = row.find('div',{"class":"span3 message-speaker"}).find('div').text
				episode_title = row.find('div',{'class':'span9 message-title'}).find('div').text
				episode_link = row.find('div',{"class":"action-download"}).find('a', href=True)
				episode_date_obj = datetime.datetime.strptime(episode_date, '%b %d, %Y')
				# print("Series Num:",n)
				# print('Message Title:',episode_title)
				# print('Message Date:',episode_date)
				# print('Message Date OBJ:',episode_date_obj.strftime('%Y-%m-%d'))
				# print('Audio Link:',episode_link['href'])
				# print('')

				episode = {
					"series_id": n,
					"title": episode_title,
					"date": str(episode_date_obj.strftime('%Y-%m-%d')),
					"link": episode_link['href']
				}
				
				print(episode)
				print('')

				episode_table.insert(episode)

			series_table.insert(series)

		else:
			
		    print("No More Sections Found!")
		    print("last serial_id:{}".format(n))
		    print("Crawling Completed!!")
		    sys.exit(1)
				
		
		time.sleep(1.25)

def series_find_cats(term):
	db = TinyDB('db_bkup.json')
	qry = Query()
	# series_table = db.table('series')
	res = db.search(qry.category == str(term))
	print(res)

def series_find_label(term):
	# Genesis
	db = TinyDB('db_bkup.json')
	qry = Query()
	# series_table = db.table('series')
	res = db.search(qry.label == str(term).lower())
	print(res)

def find_all():
	db = TinyDB('./db_bkup.json')
	series_table = db.table('episode')
	qry = Query()
	print(series_table.search(qry.label == str('Genesis')))


if __name__ == '__main__':
    fire.Fire()
    
