# Nashville Legislature

#### NSS Back End Capstone Cohort 18 by James Tonkin

## Project Goals:
1. Scrape Resolutions, Bills, Council Member stats from the [Nashville Metro Website](http://www.nashville.gov/).
2. Store this information into a Django REST Framework API.
3. Present this information using AngularJS in a front end client found [here](https://github.com/jamestonkin/nss-backend-capstone-client).

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
```

### Installing
Clone repo:

```
https://github.com/jamestonkin/nss-backend-capstone-python-django.git
```
Setting up the database:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
