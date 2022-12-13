# My Rackerrank solutions

## How to run local with docker

### Clean up

```shell
make clean-up
```

### Build image

```shell
docker build --rm -t hackerrank-image:1 .
docker image ls -a
```

```shell
docker run -it -d --name hackerrank hackerrank-image:1
docker ps
```

```shell
docker exec -it hackerrank bash
```

### Debug

```shell
make golang
```
