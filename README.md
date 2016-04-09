## QuickStart
1. Clone repository and go to the `dev` docker folder.
```bash
git clone https://gitlab.com/andrew.shvv/deluge.git
cd deluge/docker/dev
```

2. Add entry to the /etc/hosts
* If you run docker containers on the docker-machine, than check your ip and set it to the /etc/hosts
```
docker-machine ip
sudo bash -c 'echo "absortium.com <ip>" >> /etc/hosts'
```
* Otherwise set localhost
```
sudo bash -c 'echo "absortium.com localhost" >> /etc/hosts'
```

3. Run `postgres` service which serve as database.
```
docker-compose up -d postgres
```

4. Run `frontend` and make sure that service runs without errors.
```
docker-compose up frontend
```

5. Go to the `absortium.com`


## Step-by-step
1. Clone repository and go to the `dev` docker folder.
```bash
git clone https://gitlab.com/andrew.shvv/deluge.git
cd deluge/docker/dev
```

2. Build `router` - crossbar web server which proxied events to the websocket connected users.
```
docker-compose build --no-cache router
```

3. Build `frontend` - grunt server which serves static files and proxied `/api`, `/auth` request to the `backend` server.
```
docker-compose build --no-cache frontend
```

4. Run `postgres` service which serve as database.
```
docker-compose up -d postgres
```

5. Build backend server which get `/api`, `/auth`requests from the `frontend` server and process it.
```
docker-compose build --no-cache backend
```

6. Run `backend` and make sure that service runs without errors.
```
docker-compose up backend
```

7. Run `frontend` and make sure that service runs without errors.
```
docker-compose up frontend
```

8. Make sure that all services are working:
    * `router`
    * `backend`
    * `frontend`
    * `postgres`
    * `datadog` - this service currently not needed!

## Usefull commands
1. Stop all dockers containers
```
docker ps |  awk '{printf "%s\n",$1}' | xargs docker stop
```
2. Delete all docker containers
```
docker ps -a |  awk '{printf "%s\n",$1}' | grep -v -i container | xargs docker rm --force
```
3. Delete all <none> images
```
docker images -a | grep "<none>" | awk '{ printf "%s\n", $3}' | xargs docker rmi -f
```
4. Exec bash in the runnig container
```
docker exec -i -t postgres bash
```
5. Run container with `bash` command
```
docker-compose run backend bash
```
6. Flush database
```
docker-compose kill postgres
docker volume rm -f dev_dbdata
```

## Tips
1. If you use `docker-machine` than you must download project only in user direcotory.


## Backend schema
![alt tag](/docs/schema/main.png)