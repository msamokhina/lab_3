from base_client import BaseClient
from datetime import datetime, timedelta
import requests

class CatchFriends(BaseClient):
    # friends for our user
    friends = None

    def __init__(self, ID):
        self.BASE_URL = "https://api.vk.com/method/"
        self.method = "friends.get"
        self.http_method = "GET"
        params = {"user_id": ID, "order": "random", "list_id": None,
                  "count": None, "offset": None, "fields": "bdate",
                  "name_case": "nom"}
        self.friends = self.execute(params)

    # Response handler
    def response_handler(self, response):
            response.raise_for_status()

            dateOfB = []
            for x in response.json()["response"]:
                if x.get("bdate") != None:
                    #arr = datetime.strptime(x.get("bdate"), "%d.%m.%Y")
                    #dateOfB.append( datetime.now().year - arr.year )
                    arr = (x.get("bdate")).split('.')
                    if len(arr) == 3:
                        dateOfB.append(datetime.now().year - int(arr[2]))

            dateOfB.sort()
            return dateOfB

    # VK API
    def _get_data(self, parameters):
        response = None
        if self.http_method == "GET":
            response = requests.get(self.generate_url(self.method), params=parameters)

        return self.response_handler(response)