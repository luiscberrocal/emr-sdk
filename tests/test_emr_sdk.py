#!/usr/bin/env python

"""Tests for `emr_sdk` package."""

import pytest

from emr_sdk import emr_sdk
from emr_sdk.emr_sdk import EMRWebClient


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_get_token():
    fn = '/Users/luiscberrocal/PycharmProjects/emr_sdk/.env/staging_config.json'
    fn = '/Users/luiscberrocal/PycharmProjects/emr_sdk/.env/local_config.json'
    client = EMRWebClient(filename=fn)
    assert client.token is not None
    assert len(client.token) > 20
    print(f'>>>> {client.token}')


def test_get_clinic():
    fn = '/Users/luiscberrocal/PycharmProjects/emr_sdk/.env/local_config.json'
    client = EMRWebClient(filename=fn)
    response = client.get_clinic(1)
    assert response['name'] == 'Next Generation Clinic'

