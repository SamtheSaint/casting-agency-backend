# Casting Agency Backend

## Installing Dependencies

### Python 3.7.X or higher

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

### Virtual Enviornment

Working within a virtual environment is recommended whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by opening a terminal in this directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the [`./requirements.txt`](./requirements.txt) file.

### PostgreSQL Database

Follow instructions to install the latest version of postgres for your platform in the [postgres docs](http://postgresguide.com/setup/install.html)

## Required Tasks

### Setup the Database

The migrations for the database have already been included in the `./migrations` directory. To setup a database for the application, open the terminal and run:

```bash
createdb DATABASE_NAME
```

Then nagivate to the [`./setup.sh`](./setup.sh) script and set the database url environment variable. For the format of the URI, refer to the [postgres docs](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING).

```
postgresql://[user[:password]@][netloc][:port][,...][/dbname][?param1=value1&...]
```

### Run the Database Migrations

Once the database uri has been setup, the migrations can be run to setup the necessary database schema needed for the web app. Open a terminal in this directory and run:

```bash
python manage.py db upgrade
```

## Running the server

From within this directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.
