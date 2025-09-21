import requests

BASE_URL = "http://127.0.0.1:5000"

print("Home Page HTML:\n", requests.get(BASE_URL + "/").text)


breed = "beagle"
print(f"\nDog by breed ({breed}):")
print(requests.get(BASE_URL + f"/dog_by_breed?breed={breed}").json())
