# Ponies

Sample Django application

# How to configure your environment

- (Archlinux) `pacman -S python2 virtualenvwrapper postgresql`
- (Debian/Ubuntu) `apt-get install python2 virtualenvwrapper postgresql`
- `cd` to the cloned repo
- `mkvirtualenv --python=python2.7 ponies`
- `pip install -r requirements.txt`
- `echo -e "DJANGO_SECRET_KEY=\nDJANGO_DEBUG=\nDATABASE_URL=" > .env`

# Configure the database

## Local db

- (Archlinux) See https://wiki.archlinux.org/index.php/PostgreSQL
- $`sudo passwd postgres`
- $`su - postgres`
- postgres$`initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/postgres/data'`
- $`sudo systemctl start postgresql.service`
- postgres$`createuser -d -r django`
- postgres$`createdb -U django ponies`

Then get back to your virtual env and run the migrations:

- $`workon ponies`
- $`export $(cat .env)`
- $`python manage.py migrate`

## Distant db

- Open file _.env_
- Edit entry `DATABASE_URL=postgresql://<user>@<address>/<database>`

# Run the server

Your environment is now ready. To run the server, follow these steps:

- (if not done yet) `export $(cat .env)`
- run with `python manage.py runserver`
- open a web browser at http://127.0.0.1:8000/

# Get rid of that silly export

If you're tired of typing `export $(cat .env)` every time you open a terminal, try this:

- `cd` to the cloned repo
- `setvirtualenvproject`
- `echo "cdproject && export \$(cat .env)" >> $VIRTUAL_ENV/bin/postactivate`

# Create a django admin

To be able to log in http://127.0.0.1:8000/admin you will need an admin account:

- `python manage.py createsuperuser`

# Access the API

You can GET on http://127.0.0.1:8000/api/v1/pony to query the api.

