### Prior steps to run Docker make sure to reset the DB
```
 rm core/store.sqlite3
 flask db upgrade -d core/migrations/
```




### Docker Steps
1) Build Docker Images defined in the docker-compose.yml
```
docker-compose build
```
2) Create, starts the containers by detaching
```
docker-compose up -d
```
3) Kills, stops the running containers
```
docker-compose down
```
