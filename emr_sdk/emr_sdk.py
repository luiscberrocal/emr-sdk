"""Main module."""
import json
import requests


class EMRWebClient:

    def __init__(self, **kwargs):
        filename = kwargs.get('filename')
        configuration = self._get_configuration(filename)
        self.base_url = configuration.pop('base_url')
        self.token = self._get_token_data(**configuration)
        self.headers = {'Authorization': f'Bearer {self.token}',
                        'content-type': 'application/json'}
        self.errors = list()

    def _get_token_data(self, username, password, token_key):
        url = f'{self.base_url}/api/v1/token/'
        response = requests.post(url, data={'username': username, 'password': password})
        token_data = json.loads(response.text)
        return token_data.get(token_key)

    def _get_configuration(self, filename, **kwargs):
        with open(filename, 'r') as json_file:
            credentials = json.load(json_file)
        return credentials

    def get_clinic(self, clinic_id):
        # const headers = {headers: {"Authorization": `Bearer ${JWTToken}`}}
        url = f'{self.base_url}/clinic/api/v1/clinic/{clinic_id}'
        response = requests.get(url, headers=self.headers)
        data = None
        if response.status_code == 200:
            data = json.loads(response.text)
        else:
            error = dict()
            error['method'] = 'get_clinic'
            error['status_code'] = response.status_code
            error['message'] = response.text
            self.errors.append(error)
        return data


