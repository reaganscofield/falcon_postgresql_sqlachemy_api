Falcon REST API with PostgreSQL SQLAlchemy
============================================


Simple REST API using Falcon web framework.

Falcon is a high-performance Python framework for building cloud APIs, smart proxies, and app backends. More information can be found [here](https://github.com/falconry/falcon/).

Requirements
============
This project uses [virtualenv](https://virtualenv.pypa.io/en/stable/) as isolated Python environment for installation and running. Therefore, [virtualenv](https://virtualenv.pypa.io/en/stable/) must be installed. And you may need a related dependency library for a PostgreSQL database. See [install.sh](https://github.com/ziwon/falcon-rest-api/blob/master/install.sh) for details.


Installation
============

Install all the python module dependencies in requirements.txt

```
  ./install.sh
```

Start server

```
  ./bin/run.sh start
```

Deploy
=====
You need to set `APP_ENV` environment variables before deployment. You can set LIVE mode in Linux/Heroku as follows.

Linux
------
In Linux, just set `APP_ENV` to run in live mode.
```shell
export APP_ENV=live
./bin/run.sh start
```

Heroku
------
In Heroku, use the command `config:set`. (See [here](https://devcenter.heroku.com/articles/config-vars) for details)
```shell
heroku config:set APP_ENV=live
```