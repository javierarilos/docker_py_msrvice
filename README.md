# docker python microservice
Simplest possible `python` microservice, with `Bottle`. Packed and deployed into
a `docker container`.

If you need an intro on docker, you can check: [docker as a packaging environment](https://gist.github.com/javierarilos/a0f8dafdf63d65fb2c8c#file-docker-as-packaging-execution-environment-md) or `docker` documentation.

This sample is hosted in [github/javierarilos](https://github.com/javierarilos/docker_py_msrvice)

## System requirements
`docker` up and running, see: [docker/installation](https://docs.docker.com/engine/installation/)

## building the docker image
From this same directory:
```bash
$ docker build -t dpm .
```

## running the container
```bash
docker run -it --rm -p=0.0.0.0:8888:8888 dpm
```

## REST API
The application is a very simple microservice for `customers`.

`GET` a customer:
```bash
$ curl http://127.0.0.1:8888/customers/alan
```

`POST` a new customer:
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"name": "alan", "born": 1903}' http://127.0.0.1:8888/customers
```

`GET` all customers:
```bash
$ curl http://127.0.0.1:8888/customers
```
