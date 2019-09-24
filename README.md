# My Rackerrank solutions with Python


#### How to run local with docker:

Clean up:
```shell
sudo docker rm -f $(sudo docker ps -aq)
sudo docker ps -a
```

Build image:
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
