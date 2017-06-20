import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

# Connects and verifies there is a connection to the website
url = 'http://www.nashville.gov/Metro-Council/Metro-Council-Members.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print("ERROR! Site is not loading!")

# Pulls the council member data using BeautifulSoup and creates council_member list
council_members = list()

for _ in soup:
    positions = soup.find_all('div', {'class': 'councilItem'})
    name = soup.find_all('a', {'class': 'councilName'})
    email = soup.find_all('a', {'class': 'email'})

# Pulls council member first and last name and stores in council_members list
for member in name:
    if member.text.split():
        council_members.append(member.text.split())

# Pulls council members email and stores in council_members list
for k, member_email in enumerate(email):
    try:
        clean_email = member_email['href'].replace('mailto:', '')
        council_members[k].append(clean_email)

    except KeyError:
        pass

# Pulls council members district and stores in council_members list
for k, position in enumerate(positions):
    clean_position = position.find('a')
    council_members[k].append(clean_position.text)

# Cleans up middle name of Council Member District 20
for i in council_members:
    if len(i) == 5:
        del i[1]

# Cleans up Vacant Council Member District 33
for i in council_members:
    if len(i) == 2 and i[0] == 'Vacant':
        del i[0]
        i.insert(0, '')
        i.insert(1, 'Vacant')
        i.insert(2, 'Email')

# Creates pandas DataFrame of council_members and stores in SQL database
columns = ['first_name', 'last_name', 'email', 'district']
df = pd.DataFrame(council_members, columns=columns)
con = sql.connect("../db.sqlite3")
try:
    pd_sql.to_sql(df, "legislatureapi_councilmember", con, index=False)

except ValueError:
    pd_sql.to_sql(df, "legislatureapi_councilmember", con, index=False, if_exists='append')
