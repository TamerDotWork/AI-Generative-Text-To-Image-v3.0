import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": f"Bearer sk-NqpCxEPlttNZNFXKApERcy0w1qH9OT5s2ikYzn226pbFfeOl",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "dog wearing white glasses",
        "output_format": "jpeg",
    },
)
if response.status_code == 200:
    with open("./dog-wearing-glasses.jpeg", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))
