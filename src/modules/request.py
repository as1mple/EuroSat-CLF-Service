import requests


def post(file, url):
    return requests.post(url, files={"file": file})
