#!/usr/bin/env python

"""Tests for `emr_sdk` package."""

import pytest

from emr_sdk import emr_sdk
from emr_sdk.emr_sdk import EMRWebClient


@pytest.fixture(scope='session')
def emr_client():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    fn = '/Users/luiscberrocal/PycharmProjects/emr_sdk/.env/staging_config.json'
    fn = '/Users/luiscberrocal/PycharmProjects/emr_sdk/.env/local_config.json'
    client = EMRWebClient(filename=fn)
    return client


def test_get_token(emr_client):
    assert emr_client.token is not None
    assert len(emr_client.token) > 20
    print(f'>>>> {emr_client.token}')


def test_get_clinic(emr_client):
    response = emr_client.get_clinic(1)
    assert response['name'] == 'Next Generation Clinic'


def test_get_clinic_invalid_id(emr_client):
    clinic_data = emr_client.get_clinic(19000)
    assert clinic_data is None
    assert len(emr_client.errors()) == 1
    assert emr_client.errors()[0]['method'] == 'get_clinic'
    assert emr_client.errors()[0]['status_code'] == 404
    assert 'Not found' in emr_client.errors()[0]['message']
