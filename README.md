## QuickStart
* Clone repository, set environment variables and go to the `dev` docker folder.
```bash
$ git clone --recursive https://github.com/absortium/deluge.git
$ source deluge/environment/secrets.sh
$ cd deluge/docker/dev
```
* Add entry to the /etc/hosts
   * If you run docker containers on the docker-machine, than check your ip and set it to the /etc/hosts
   ```
   $ docker-machine ip
   $ sudo bash -c 'echo "absortium.com <ip>" >> /etc/hosts'
   ```
   * Otherwise set localhost
   ```
   $ sudo bash -c 'echo "absortium.com localhost" >> /etc/hosts'
   ```
* Run `postgres` service which serve as database.
```
$ docker-compose up -d postgres
```
* Run `frontend` and make sure that service runs without errors.
```
$ docker-compose up frontend
```
* Go to the `absortium.com`

## Step-by-step
* Clone repository, set environment variables and go to the `dev` docker folder.
```bash
$ git clone --recursive https://github.com/absortium/deluge.git
$ source deluge/environment/secrets.sh
$ cd deluge/docker/dev
```
* Build `router` - crossbar web server which proxied events to the websocket connected users.
```
$ docker-compose build --no-cache router
```

* Build `frontend` - grunt server which serves static files and proxied `/api`, `/auth` request to the `backend` server.
```
$ docker-compose build --no-cache frontend
```

* Run `postgres` service which serve as database.
```
$ docker-compose up -d postgres
```

* Build backend server which get `/api`, `/auth`requests from the `frontend` server and process it.
```
$ docker-compose build --no-cache backend
```

* Run `backend` and make sure that service runs without errors.
```
$ docker-compose up backend
```

* Run `frontend` and make sure that service runs without errors.
```
$ docker-compose up frontend
```

* Make sure that all services are working:
    * `router`
    * `backend`
    * `frontend`
    * `postgres`
    * `datadog` - this service currently not needed!

## Usefull commands
* Stop all dockers containers
```
$ docker ps |  awk '{printf "%s\n",$1}' | xargs docker stop
```
* Delete all docker containers
```
$ docker ps -a |  awk '{printf "%s\n",$1}' | grep -v -i container | xargs docker rm --force
```
* Delete all <none> images
```
$ docker images -a | grep "<none>" | awk '{ printf "%s\n", $3}' | xargs docker rmi -f
```
* Exec bash in the runnig container
```
$ docker exec -i -t postgres bash
```
* Run container with `bash` command
```
$ docker-compose run backend bash
```
* Flush database
```
$ docker-compose kill postgres
$ docker volume rm -f dev_dbdata
```

## Tips
* If you use `docker-machine` than you must download project only in user direcotory.


## Backend schema
![alt tag](/docs/schema/main.png)
