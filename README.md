# EuroSat~[CLF]

> The service provides the ability to classify land in geospatial images.

## DVC

> Install requirements => pip install -r requirements_dvc.txt
>
> Downloads tracked data from remote storage to the cache => dvc pull

## FastAPI

> Install requirements => pip install -r requirements_API.txt
>
> Run FastAPI => uvicorn src.api_run:app --host=0.0.0.0 --port=${PORT:-5011}
> 
> Docker build => sudo docker build -t fastapi_eurosat -f DOCKER .
>
> Docker Run => sudo docker run -p 8080:5011 -v /{full path to project}/logs/:/app/logs/ fastapi_eurosat
 

## Streamlit

> Docker build => sudo docker build -t streamlit -f DOCKER_STREAMLIT .
> 
> Docker Run => sudo docker run -p 8081:8501 -e IP={IP FAST_API} -e PORT={PORT FAST_API} -v /{full_path_to_project}/logs/:/app/logs/ streamlit

