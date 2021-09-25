"""Main module."""
import json
import requests


class EMRWebClient:

    def __init__(self,  **kwargs):
        filename = kwargs.get('filename')
        configuration = self._get_configuration(filename)
        self.base_url = configuration.pop('base_url')
        self.token = self._get_token_data(**configuration)

    def _get_token_data(self, username, password, token_key):
        url = f'{self.base_url}/api/v1/token/'
        response = requests.post(url, data={'username': username, 'password': password})
        token_data = json.loads(response.text)
        return token_data.get(token_key)

    def _get_configuration(self, filename, **kwargs):
        with open(filename, 'r') as json_file:
            credentials = json.load(json_file)
        return credentials
