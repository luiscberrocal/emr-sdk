"""Main module."""
import json
import requests


class EMRWebClient:

    def __init__(self,  **kwargs):
        filename = kwargs.get('filename')
        confiuration = self._get_configuration(filename)
        self.base_url = confiuration['base_url']
        r = self._get_token_data(username=confiuration['username'], pwd=confiuration['password'])

    def _get_token_data(self, username, pwd):
        url = f'{self.base_url}/api/v1/token/'
        response = requests.post(url, data={'username': username, 'password': pwd})
        token_data = json.loads(response.text)
        return token_data

    def _get_configuration(self, filename, **kwargs):
        with open(filename, 'r') as json_file:
            credentials = json.load(json_file)
        return credentials
