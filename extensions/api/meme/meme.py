import requests

username="CallMeQan"
password="imquanthememe"
userAgent=""

meme_id = {
    "woman_yelling_at_cat": "188390779",
    "scared_cat": "4173692",
    "Too_damm_high": "61580"
}
# images = requests.get("https://api.imgflip.com/get_memes").json()["data"]["memes"]

class meme():
    def __init__(self):
        pass

    def __regenerate_caption_image__(self, endpoint_id: str, text0: str, text1: str) -> str:
        URL = 'https://api.imgflip.com/caption_image'
        data = {
            'username': username,
            'password': password,
            'template_id': endpoint_id,
            'text0': text0,
            'text1': text1
        }
        response = requests.request("GET", url=URL, data=data)
        return response.json()["data"]["url"]
    
    def waiting_skeleton(self, text0: str, text1: str):
        endpoint_id = "4087833"
        return self.__regenerate_caption_image__(endpoint_id, text0, text1)
    
    def woman_yelling_at_cat(self, text0: str, text1: str):
        endpoint_id = "188390779"
        return self.__regenerate_caption_image__(endpoint_id, text0, text1)
    
    def scared_cat(self, text0: str, text1: str):
        endpoint_id = "4173692"
        return self.__regenerate_caption_image__(endpoint_id, text0, text1)
    