"""Main module."""
import json
from datetime import datetime

import requests


class ErrorHandler:

    def __init__(self, **kwargs):
        self.auto_reset = kwargs.get('auto_reset', False)
        self.errors = list()

    def handle_error(self, caller_function, response):
        if self.auto_reset:
            self.errors.clear()
        error = dict()
        error['method'] = caller_function
        error['status_code'] = response.status_code
        error['message'] = response.text
        error['time_stamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:$S')
        self.errors.append(error)


class EMRWebClient:

    def __init__(self, **kwargs):
        filename = kwargs.get('filename')
        configuration = self._get_configuration(filename)
        self.base_url = configuration.pop('base_url')
        self.token = self._get_token_data(**configuration)
        self.headers = {'Authorization': f'Bearer {self.token}',
                        'content-type': 'application/json'}
        self.error_handler = ErrorHandler()

    def _get_token_data(self, username, password, token_key):
        url = f'{self.base_url}/api/v1/token/'
        response = requests.post(url, data={'username': username, 'password': password})
        token_data = json.loads(response.text)
        return token_data.get(token_key)

    def _get_configuration(self, filename, **kwargs):
        with open(filename, 'r') as json_file:
            credentials = json.load(json_file)
        return credentials

    def errors(self):
        return self.error_handler.errors

    def get_clinic(self, clinic_id):
        url = f'{self.base_url}/clinic/api/v1/clinic/{clinic_id}'
        response = requests.get(url, headers=self.headers)
        data = None
        if response.status_code == 200:
            data = json.loads(response.text)
        else:
            self.error_handler.handle_error('get_clinic', response)
        return data
