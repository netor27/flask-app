[![Python](https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6--dev-blue.svg)]()
[![Requirements Status](https://requires.io/github/netor27/flask-app/requirements.svg?branch=master)](https://requires.io/github/netor27/flask-app/requirements/?branch=master)
[![Travis](https://travis-ci.org/netor27/flask-app.svg?branch=master)](https://travis-ci.org/netor27/flask-app)
[![Coverage](https://codecov.io/gh/netor27/flask-app/branch/master/graph/badge.svg)](https://codecov.io/gh/netor27/flask-app)

Code forked from [https://github.com/brennv/flask-app](brennv/flask-app). Deploy configuration changed for test purposes

# flask-app

Example app for demonstrating continuos integration/continuos deployment (CI/CD) workflows -- inspired by [dockercloud-quickstart-python](https://github.com/docker/dockercloud-quickstart-python).

The example flask app connects to a [redis](http://redis.io/) instance and displays a simple visit counter and the hostname of the docker container serving the app.

## Getting started

Install [docker](https://docs.docker.com/engine/installation/) and run:

```shell
docker-compose up
# docker-compose stop
```

Otherwise, for the standalone web service:

```shell
pip install -r requirements.txt
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

## Development

Create a new branch off the **develop** branch for features or fixes.

After making changes rebuild images and run the app:

```shell
docker-compose build
docker-compose run -p 5000:5000 web python app.py
# docker stop flaskapp_redis_1
```

## Tests

Standalone unit tests run with:

```shell
pip install pytest pytest-cov pytest-flask
pytest --cov=web/ --ignore=tests/integration tests
```

Integration and unit tests run with:

```shell
docker-compose -f test.yml -p ci build
docker-compose -f test.yml -p ci run test python -m pytest --cov=web/ tests
# docker stop ci_redis_1 ci_web_1
```

Commits tested via [travis-ci.org](https://travis-ci.org/netor27/flask-app). Test coverage reported to [codecov.io](https://codecov.io/gh/netor27/flask-app). Requirements inspected with [requires.io](https://requires.io/github/netor27/flask-app/requirements).

After testing, submit a pull request to merge changes with **develop**.