# react-django-jwt-auth-backened
django backened with rest framework to handle signup/ login / token verification

## [Frontend code here](https://github.com/coderpd/react-django-jwt-auth-frontend)
## [Frontend hosted here](http://coderpd.me/react-django-jwt-auth-frontend/)

# How to use
1. `pipenv shell` to create virtual python environment
2. `pipenv install` to install all dependencies
3. create `.env` file in /backends/ folder, and update your local environment variables
### Environment Variables you need
#### a) SECRET_KEY
#### b) DBENGINE
#### c) DBHOST
#### d) DBNAME
#### e) DBUSER
#### f) DBPASS
settings.py needs these environment variables, read settings.py for more insight
App won't run without these variables

When deploying to cloud, add these varibales in app configuration

4. `python manage.py makemigrations`
   `python manage.py migrate`
   `python manage.py runserver`
