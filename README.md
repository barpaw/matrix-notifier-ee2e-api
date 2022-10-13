# synapse-notifier-ee2e-api
API for sending messages in encrypted rooms (synapse matrix)

## About
This project allows you to send messages in encrypted matrix rooms using a web api.

## Endpoints

`Send message to ee2e matrix room`

- POST /send-message

```
curl -X 'POST' \
  'http://localhost:8001/send-message' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "matrixHomeserverURL": "string",
  "matrixHomeserverUser": "string",
  "matrixHomeserverPasswd": "string",
  "matrixHomeserverRoom": "string",
  "message": "string"
}
```

`Healthcheck`
- GET /health
  
`Swagger`
- GET /docs
  
`Redoc`
- GET /redoc
  

## Usage

- Create a matrix user then join the room where you want to send messages and logout
- ```docker build -t barpaw/synapse-notifier-ee2e-api:mybuild . ```

- ```docker run -d --rm -p 8001:8001 barpaw/synapse-notifier-ee2e-api:mybuild ```

- Try it http://localhost:8001/docs

## Dependecies

- Docker
  
### Project python packages
- [matrix-nio[e2e]](https://github.com/poljar/matrix-nio)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [pydantic](https://github.com/pydantic/pydantic)
- [uvicorn](https://github.com/encode/uvicorn)

### 

## Docker Hub

[barpaw/synapse-notifier-ee2e-api](https://hub.docker.com/r/barpaw/synapse-notifier-ee2e-api)

### Platforms

AMD64
- ```docker run -d --rm -p 8001:8001 barpaw/synapse-notifier-ee2e-api:0.0.1-amd64 ```

ARM64
- ```docker run -d --rm -p 8001:8001 barpaw/synapse-notifier-ee2e-api:0.0.1-arm64 ```

