import json
import requests

def cat():
    cat_response = requests.get("https://api.thecatapi.com/v1/images/search")
    # print(cat_response.text)
    # print(json.loads(cat_response.text)[0]["url"])
    cat_image = json.loads(cat_response.text)[0]["url"]
    # print(cat_image)
    return cat_image


def dog():
    dog_response = requests.get("https://dog.ceo/api/breeds/image/random")
    # print(dog_response.text)
    # print(json.loads(dog_response.text)["message"])
    dog_image = json.loads(dog_response.text)["message"]
    # print(dog_image)
    return dog_image


def fox():
    fox_response = requests.get("https://randomfox.ca/floof/")
    # print(fox_response.text)
    # print(json.loads(fox_response.text)["image"])
    fox_image = json.loads(fox_response.text)["image"]
    # print(fox_image)
    return fox_image
