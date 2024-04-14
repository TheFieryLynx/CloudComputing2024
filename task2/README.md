<body>
<h1 align="center">~ 𝓒𝓵𝓸𝓾𝓭 𝓒𝓸𝓶𝓹𝓾𝓽𝓲𝓷𝓰 2024. 𝓣𝓪𝓼𝓴 2 ~</h1>
<div>

* Курс: Облачные вычисления
* Факультет: ВМК МГУ
* Задание 2

## Dependencies:
* minikube
* kubectl
* docker

## Info:
Code of the first task was taken as the api and database. The corresponding directories were moved to task 2 using symlinks

## Usage:
### Deploy:
1. First run minikube cluster:
    ```
    make minikube/start
    ```

2. Deploy services
    ```
    make kubectl/deploy/all
    ```
3. Run tunnel to access api
    ```
    make run
    ```
    Output (smth like this):
    ```
    |-----------|------|----------------|---------------------------|
    | NAMESPACE | NAME |  TARGET PORT   |            URL            |
    |-----------|------|----------------|---------------------------|
    | default   | api  | api-port/20243 | http://192.168.49.2:30000 |
    |-----------|------|----------------|---------------------------|
    🏃  Starting tunnel for service api.
    |-----------|------|-------------|------------------------|
    | NAMESPACE | NAME | TARGET PORT |          URL           |
    |-----------|------|-------------|------------------------|
    | default   | api  |             | http://127.0.0.1:62173 |
    |-----------|------|-------------|------------------------|
    ```

    To access api from example use http://127.0.0.1:62173/docs url (your port might be different)

    **NOTE:** Perhaps this is necessary only on non-Linux systems (development is done on macOS m1)

    On linux systems you can get url by:
    ```
    minikube service server-app --url
    ```

### Additional:
* Delete minikube cluster:
    ```angular2html
    make minikube/delete
    ```
* Access kubernetes dashboard:
    ```
    make minikube/dashboard
    ```
* Delete all deployments:
    ```
    make kubectl/delete/all
    ```
* Get all pods:
    ```
    make kubectl/pods
    ```
* Delete services (all database data will be saved)
    ```
    make kubectl/delete/services
    ```
* Deploy deleted services
    ```
    make kubectl/deploy/services
    ```

## Api usage
[Here](../task1/api/README.md)

**NOTE:** change base url to the one that was generated by tunnel
    