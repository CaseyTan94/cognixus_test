# cognixus_test
Backend software engineer take home test from Cognixus

## Description
A pretty simplified Docker Compose workflow that sets up a Django REST container and a database container.

## Getting Started
To get started, first clone this repository by running `git clone https://github.com/CaseyTan94/cognixus_test.git`

Next do `docker-compose build` to build the docker image

After that pull database image from my dockerhub by running `docker pull caseytan/postgres`

Then bring the docker container up with `docker-compose up`

The web service will run at port 8000 e.g. `http://127.0.0.1:8000`

## Using TODO API
To use the API we first have to get the authencation token by login using Github

Using `curl -I http://127.0.0.1:8000/auth/github/url/` will return redirection URL e.g.
```
HTTP/1.1 302 Found
Location: https://github.com/login/oauth/authorize?client_id=6d2098b0d015605ff492&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fauth%2Fgithub%2Fcallback%2F&scope=&response_type=code&state=p00Sh6Yy11mW
```
connecting to this url will displays this OAuth2 authorization page

After click on authorize to the app a code with redirect show as following
`http://127.0.0.1:8000/auth/github?code=759acf0548b44ba6fcd3&state=p00Sh6Yy11mW`

Next using code you get do a login post to get the API token 
`curl -X POST http://127.0.0.1:8000/auth/github/ -d code=759acf0548b44ba6fcd3`

example return
`{"key":"39266e6cc90a43830d14a5758efb2c1dd8608877"}`

## API documentation
The following API to interact with todo_list

List API
```http
GET /todo/
```
Responses:
```json
[
    {
        "id": integer,
        "title": string,
        "body": string,
        "is_completed": bool,
        "owner": string
    },
]
```
---
Create API
```http
POST /todo/create/
```
Request:
```json
{
    "title": string,
    "body": string
}
```
Responses:
```json
{
    "id": integer,
    "title": string,
    "body": string,
    "is_completed": bool,
    "owner": string
}
```
---
Update API
```http
PUT /todo/update/{id}
```
Request:
```json
{
    "title": string,
    "body": string,
    "is_completed": bool,
}
```
Responses:
```json
{
    "id": integer,
    "title": string,
    "body": string,
    "is_completed": bool,
    "owner": string
}
```
---
Delete API
```http
DELETE /todo/delete/{id}
```
No request body required