import requests

class BaseClient:
    # URL vk api
    BASE_URL = None
    # method vk api
    method = None
    # GET, POST, ...
    http_method = None

    # GET
    def get_params(self):
        return None

    # POST
    def get_json(self):
        # _get_data
        #response.json()
        return None

    # HTTP
    def get_headers(self):
        # _get_data
        #response.headers['content-type']
        return None

    # url
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # VK API
    def _get_data(self, parameters):
        response = None
        return self.response_handler(response)

    # VK API
    def response_handler(self, response):
        return response


    # Start client
    def execute(self, parameters):
        return self._get_data(
            parameters
        )