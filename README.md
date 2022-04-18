## Setup

First clone the repository:

```sh
$ git clone https://github.com/nikitapt63/car-showroom
$ cd car_showroom
```

Clone `.env.example` file, rename it to `.env`.

Run `PostgreSQL` docker container localy:

```sh
$ docker run --name db -p 5432:5432 --env-file ./.env.example -d postgres:13.3
```

And run the Django server:

```sh
$ cd car_showroom
$ python manage.py runserver
```