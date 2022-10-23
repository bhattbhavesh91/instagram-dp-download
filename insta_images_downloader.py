import requests
import os
import json
import shutil

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}

INSTA_URL = "https://www.instagram.com/"
USER_ID = "rogerfederer"
TAIL = "/?__a=1"

URL = INSTA_URL + USER_ID + TAIL
URL = INSTA_URL + USER_ID + TAIL
URL = INSTA_URL + USER_ID + TAIL
URL = INSTA_URL + USER_ID + TAIL
URL = INSTA_URL + USER_ID + TAIL
URL = INSTA_URL + USER_ID + TAIL
URL = INSTA_URL + USER_ID + TAIL

response = requests.get(URL, headers=header).json()

image_location = response["graphql"]["user"]["profile_pic_url"]
hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]

image_location_response = requests.get(image_location, stream=True)
with open("standard_img.jpg", "wb") as out_file:
    shutil.copyfileobj(image_location_response.raw, out_file)

hd_image_response = requests.get(hd_image_location, stream=True)
with open("hd_img.jpg", "wb") as out_file:
    shutil.copyfileobj(hd_image_response.raw, out_file)
