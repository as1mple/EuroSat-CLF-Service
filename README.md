# EuroSat~[CLF]

> The API provides the ability to classify land in geospatial images.

## DVC

> Install requirements => pip install -r requirements_dvc.txt
>
> Downloads tracked data from remote storage to the cache => dvc pull

## FastAPI

> Install requirements => pip install -r requirements_API.txt
>
> Run FastAPI => uvicorn src.api_run:app --host=0.0.0.0 --port=${PORT:-5011}
> 
> Docker build => sudo docker build -t fastapi_eurosat -f DOCKER_FASTAPI .
>
> Docker Run => sudo docker run -p 8080:5011 -v /{full path to project}/logs/:/app/logs/ fastapi_eurosat
 
