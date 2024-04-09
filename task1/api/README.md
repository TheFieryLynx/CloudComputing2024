# Api documentation

FastApi docs location: http://localhost:20243/docs (or you use your custom port, which was exposed in the docker-compose file)

## Requests

### From /docs link

This is the easiest way to send requests is to use docs. Just choose request - than _Try it out!_ button - fill parameters and click _execute_ button

### Using curl
1) Creating new user: **POST /api/v1/users/**
```curl -X 'POST' \
curl -X 'POST' \
  'http://localhost:20243/api/v1/users/?email=example%40gmail.com&first_name=Biba&last_name=Boba' 
  ```
2) Get user by id: **GET /api/v1/users/{user_id}**
```
curl -X 'GET' \
  'http://localhost:20243/api/v1/users/1'
```
3) Get user list: **GET /api/v1/users/**
```
curl -X 'GET' \
  'http://localhost:20243/api/v1/users/'
```