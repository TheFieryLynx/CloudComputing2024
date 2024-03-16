<body>
<h1 align="center">~ 𝓒𝓵𝓸𝓾𝓭 𝓒𝓸𝓶𝓹𝓾𝓽𝓲𝓷𝓰 2024 ~</h1>
<div>

* Курс: Облачные вычисления
* Факультет: ВМК МГУ

## Dependencies:
* python 3.11
* poetry
* docker
* make

## Usage
Poetry should be installed:
``` 
pip install poetry
```


Makefile is used to manage the project:
* **Building**:
```
make compose/build
```
* **Running** (you can run this target without building first, building target is a dependency of this):
```
make compose/up
```
Or if you want to run in the background:
```
make compose/up/d
```
* **Stopping**
```
make compose/stop
```
* **Removing** containers
```
make compose/down
```
Or if you want to remove also MySql volume:
```
make compose/down/full
```

### For local development
Poetry should be installed:
``` 
pip install poetry
```

* Create venv and install dependencies:
``` 
make local/api/.venv
```

* Run uvicorn api (without database)
``` 
make local/api/run
```

## Api usage
[Here](api/README.md)