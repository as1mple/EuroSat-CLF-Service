# EuroSat~[CLF]

> The service provides the ability to classify land in geospatial images.

## DVC

``` bash
pip install -r requirements_dvc.txt # => Install requirements
```

``` bash
dvc pull # => Downloads tracked data from remote storage to the cache
```

## FastAPI

``` bash
pip install -r requirements_API.txt # => Install requirements
```

``` bash
uvicorn src.api_run:app --host=0.0.0.0 --port=${PORT:-5011} # => Run FastAPI
```

``` bash
sudo docker build -t fastapi_eurosat -f Dockerfile . # => Docker build
```

```bash 
sudo docker run -p 8080:5011 -v /{full path to project}/logs/:/app/logs/ fastapi_eurosat # => Docker Run
```

## Streamlit

```bash 
sudo docker build -t streamlit -f DOCKER_STREAMLIT . # => Docker build
```

``` bash
sudo docker run -p 8081:8501 -e IP={IP FAST_API} -e PORT={PORT FAST_API} -v /{full_path_to_project}/logs/:/app/logs/ streamlit # => Docker Run  
```
