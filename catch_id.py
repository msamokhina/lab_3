from base_client import BaseClient
import requests


class CatchID(BaseClient):
    # ID user vk.com
    ID = None

    def __init__(self, username):
        self.BASE_URL = "https://api.vk.com/method/"
        self.method = "users.get"
        self.http_method = "GET"
        params = {"user_ids": username, "fields": "", "name_case": "nom"}
        self.ID = self.execute(params)

    # Response handler
    def response_handler(self, response):
        try:
            response.raise_for_status()
            if len(response.json()["response"]) > 0:
                return response.json()["response"][0]["uid"]
            else:
                return None
        except requests.exceptions as err:
            print('Oops. Something occured')
            print(err)

    # VK API
    def _get_data(self, parameters):
        response = None
        if self.http_method == "GET":
            response = requests.get(self.generate_url(self.method), params=parameters)

        return self.response_handler(response)
