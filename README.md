# Git Users

Simple frontend and a web server for retrieving, storing, and displaying information about GitHub users from GitHub’s publicly available endpoint

## How to use

To launch git users use the following command.
```
docker compose up --build
```
Service wil be available in http://localhost:5000/

Mongodb shell can be accessed directly with:
```
docker exec -it $(docker ps --filter "ancestor=mongo:latest" -q) mongosh -u myuser -p mypassword
```
Flask command to refresh old entries can be run by connecting app container:
```
docker exec -it $(docker ps --filter "ancestor=github-usersrepos-app" -q) /bin/sh

flask cmd update_entries
```

## Tasks

- [X] Create minimal flask app
- [X] Connect app to retrieve results from external api
- [X] Set templates to load webpages.
- [X] Set some db to store results.
- [X] Use docker to load app.
- [X] Generate users update command.
