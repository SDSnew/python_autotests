import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "USER_TOKEN"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "37588"


def test_status_code():
    response = requests.get(url=f"{URL}/trainers", headers=HEADER)
    assert response.status_code == 200


def test_my_name():
    response = requests.get(
        url=f"{URL}/trainers", headers=HEADER, params={"trainer_id": TRAINER_ID})
    assert response.json()["data"][0]["id"] == TRAINER_ID
