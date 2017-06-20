import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql


minutes_link_list = list()

# Connects and verifies there is a connection to the website
url_for_minutes_page = 'http://www.nashville.gov/Metro-Clerk/Legislative/Minutes.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

response = requests.get(url_for_minutes_page, headers=headers)

if response.status_code == 200:
    soup_links = BeautifulSoup(response.content, 'html.parser')
else:
    print("ERROR! Site is not loading!")

# Pulls links to each meeting minutes for current administration using BeautifulSoup
minutes_2017 = soup_links.find_all('div', attrs={"class": "ShowFilesColumn"})[0].find_all('a')
minutes_2016 = soup_links.find_all('div', attrs={"class": "ShowFilesColumn"})[1].find_all('a')
minutes_2015 = soup_links.find_all('div', attrs={"class": "ShowFilesColumn"})[2].find_all('a')

for i in minutes_2017:
    minutes_link_list.append([i['href']])

for i in minutes_2016:
    minutes_link_list.append([i['href']])

for i in minutes_2015[:6]:
    minutes_link_list.append([i['href']])

print(minutes_link_list)

for link in minutes_link_list:
    # print(link[0])
    url_for_minutes_page = link[0]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    response = requests.get(url_for_minutes_page, headers=headers)

    if response.status_code == 200:
        html = BeautifulSoup(response.content, 'html.parser')
    else:
        print("ERROR! Site is not loading!")

    """
    Program will script the count votes page.
    """

    # Get all the <a>'s
    a_tags = html.find_all('a')

    vote_list = list()

    for bills in a_tags:
        each_bill = bills.text.split(' ')
        if each_bill[-1] == '':
            del each_bill[-1]

        del each_bill[:-1]
        # print(each_bill)

    for i in a_tags:

        # The resolution summary is the very next <p> of the <a>.
        p_tag = i.find_next('p')
        p_content = p_tag.text

        # Making sure that the summary contains votes looking for the "Ayes" in the content.
        if 'Ayes' in p_content:
            vote_list.append([p_content])

    # Counting "Ayes" votes
    for i in vote_list:
        ayes_count = list()
        split_sentence = i[0].split(' ')
        ayes_key = split_sentence.index('“Ayes”')
        for v in split_sentence[ayes_key:]:
            if v == '“Noes”':
                break
            if v != '':
                ayes_count.append(v)
        del ayes_count[-1]
        del ayes_count[0]
        print(ayes_count)
        print(len(ayes_count) - 1)

