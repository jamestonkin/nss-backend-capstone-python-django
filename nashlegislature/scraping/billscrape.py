import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql


bill_list = list()

# Connects and verifies there is a connection to the website
url = 'http://www.nashville.gov/Metro-Clerk/Legislative/Ordinances/2015-2019.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print("ERROR! Site is not loading!")

# Pulls bill data from p tags using BeautifulSoup
bill_name = soup.find('div', attrs={"class": "Normal"}).find_all('p')


# Pushes text in <p> tags into bill_list
for i in bill_name:
    link = i.find('a', href=True)
    if link:
        bill = i.a.extract()
        bill_list.append([link['href'], bill.text, i.text])

bill_list = [[x.replace('ORDINANCE ', '') for x in l] for l in bill_list]
bill_list = [[x.replace('SUBSTITUTE ', '') for x in l] for l in bill_list]
bill_list = [[x.replace('SECOND ', '') for x in l] for l in bill_list]
bill_list = [[x.replace('THIRD ', '') for x in l] for l in bill_list]
del bill_list[0]

# Saves bill data to SQLite database
columns = ['link_to_bill', 'name', 'synopsis']
df = pd.DataFrame(bill_list, columns=columns)
con = sql.connect("../db.sqlite3")
try:
    pd_sql.to_sql(df, "website_billlegislationsynopsis", con, index=False)

except ValueError:
    pd_sql.to_sql(df, "website_billlegislationsynopsis", con, index=False, if_exists='append')
