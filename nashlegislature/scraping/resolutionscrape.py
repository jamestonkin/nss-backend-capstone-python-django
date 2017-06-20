import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql


resolution_list = list()

# Connects and verifies there is a connection to the website
url = 'http://www.nashville.gov/Metro-Clerk/Legislative/Resolutions/2015-2019.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print("ERROR! Site is not loading!")

# Pulls resolution data from p tags using BeautifulSoup
resolution_name = soup.find('div', attrs={"class": "Normal"}).find_all('p')

# Gets all links, resolution names, and resolution synopsis and adds to resolution_list
for i in resolution_name:
    link = i.find('a', href=True)
    if link:
        resolution = i.a.extract()
        resolution_list.append([link['href'], resolution.text, i.text])

resolution_list = [[x.replace('RESOLUTION ', '') for x in l] for l in resolution_list]
resolution_list = [[x.replace('SUBSTITUTE ', '') for x in l] for l in resolution_list]

# Saves resolution data to SQLite database
columns = ['link_to_resolution', 'name', 'synopsis']
df = pd.DataFrame(resolution_list, columns=columns)
con = sql.connect("../db.sqlite3")
try:
    pd_sql.to_sql(df, "website_resolutionlegislationsynopsis", con, index=False)

except ValueError:
    pd_sql.to_sql(df, "website_resolutionlegislationsynopsis", con, index=False, if_exists='append')
