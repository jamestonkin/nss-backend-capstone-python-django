# Nashville Legislature

#### NSS Back End Capstone Cohort 18 by James Tonkin

## Project Goals:
1. Scrape Resolutions, Bills, Council Member, Voting stats from the [Nashville Metro Website](http://www.nashville.gov/).
2. Store this information into a SQL database using pandas.
3. Present this information using Django Framework.

Voting Screenshot:
![voting screenshot](images/voting_page.png?raw=true)

## Instructions
Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django:
```
pip install django
```
Install Dependencies:
```
pip install requests
pip install beautifulsoup4
pip install lxml
pip install pandas
```

### Installing
Clone repo:

```
https://github.com/jamestonkin/nss-backend-capstone-python-django.git
```
Setting up the database:
Transverse to the topmost nashlegislature directory
```
python manage.py makemigrations nashlegislature
```
```
python manage.py migrate
```
Transverse to the scraping directory.
```
python councilscrape.py
```
```
python billscrape.py
```
```
python resolutionscrape.py
```
```
python votingscrape.py
```
Transverse to the topmost nashlegislature directory
```
python manage.py runserver
```