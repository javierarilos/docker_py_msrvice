# docker python microservice
Simplest possible `python` microservice, with `Bottle`. Packed and deployed into
a `docker container`.

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

