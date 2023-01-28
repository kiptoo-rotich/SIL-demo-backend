#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Description
This is a backend application for accepting post and get requests from users to Album, Photo and User models.

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.9 manage.py runserver`
* Access the live site using the local host provided

## End points
```bash
127.0.0.1:8000/api/albums
```

```bash
127.0.0.1:8000/api/photos
```

```bash
127.0.0.1:8000/api/user
```

```bash
127.0.0.1:8000/api/register
```

```bash
127.0.0.1:8000/api/login
```

```bash
127.0.0.1:8000/api/logout
```

```bash
127.0.0.1:8000/api/logoutall
```

## Getting started

### Prerequisites
* python3.9
* virtual environment
* pip
* postgresql
  

#### Clone the Repo and rename it to suit your needs.
```bash
git clone `https://github.com/kiptoo-rotich/SIL-demo-backend`
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.9 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='<your database name>'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.9 manage.py check
python manage.py makemigrations demo
python3.9 manage.py sqlmigrate demo 0001
python3.9 manage.py migrate
```

#### Run the app
```bash
python3.9 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test projects`
        
## Built With

* [Python3.9](https://docs.python.org/3/)
* Django==4.1.5
* Postgresql 
* djangorestframework==3.14.0


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)