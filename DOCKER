FROM python:3.8
ARG DEBIAN_FRONTEND=noninteractive

COPY requirements_inf.txt ./requirements_inf.txt

RUN python -m pip install -U pip && \
    python -m pip install -r requirements_inf.txt && \
    python -m pip cache purge

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./ /app/

WORKDIR /app/

CMD dvc pull && uvicorn src.api_run:app --host=0.0.0.0 --port=${PORT:-5011}
