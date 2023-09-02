import requests
from datetime import datetime


PIXELA_ENDPOINT = "https://pixe.la/v1"
TOKEN = "your token"
USERNAME = "your username"

USER_URL = f"{PIXELA_ENDPOINT}/users"
USER_CONFIGS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response_user = requests.post(url=PIXELA_USER, json=PIXELA_PARAMETERS)
# response_user.raise_for_status()

GRAPH_ID = "run11"
GRAPH_URL = f"{USER_URL}/{USERNAME}/graphs"
GRAPH_CONFIGS = {
    "id": GRAPH_ID,
    "name": "HadiRun",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}
# response_graph = requests.post(url=GRAPH_URL, json=GRAPH_CONFIGS, headers=HEADERS)
# print(response_graph.json())

date = datetime.now()
running_distance = float(input("How many Km did you run today? "))

SET_URL = f"{GRAPH_URL}/{GRAPH_ID}"
SET_CONFIGS = {
    "date": date.strftime("%Y%m%d"),
    "quantity": f"{running_distance}"
}

response_set = requests.post(url=SET_URL, json=SET_CONFIGS, headers=HEADERS)
if response_set.status_code > 299:
    while response_set.status_code > 299:
        response_set = requests.post(url=SET_URL, json=SET_CONFIGS, headers=HEADERS)
print(response_set.json()["message"])

DELETE_URL = f"{SET_URL}/{date.strftime('%Y%m%d')}"
# response_delete = requests.delete(url=DELETE_URL, headers=HEADERS)
# print(response_delete.text)
