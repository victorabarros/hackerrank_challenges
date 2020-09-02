# My Rackerrank solutions

## How to run local with docker

### Clean up

```shell
make clean-up
```

### Build image

```shell
sudo docker build --rm -t hackerrank-image:1 .
sudo docker image ls -a
```

```shell
sudo docker run -it -d --name hackerrank hackerrank-image:1
sudo docker ps
```

```shell
sudo docker exec -it hackerrank bash
```

### Debug

```shell
make golang
```
