"""
Base test case
"""

import json
import unittest
from unittest import mock
from unittest.mock import MagicMock

import mongomock
import pymongo
from flask import Flask

from src.handlers.routes import configure_routes
from src.test.raw import INITIAL_DATA, TEST_VALID_WORKFLOW, TEST_NOT_VALID_WORKFLOW, TEST_STEPS_VALID_WORKFLOW


class ApiBaseTest(unittest.TestCase):

    app = Flask(__name__)
    mongo = mock.Mock()

    configure_routes(app, mongo)
    client = app.test_client()

    url = ''


class TestAccountsAPI(ApiBaseTest):
    url = "/accounts"
    data = INITIAL_DATA

    def setUp(self):
        self.mongo.db.accounts.insert_many = MagicMock(
            name='insert_many')

    def test_post(self):
        response = self.client.post(self.url, data=json.dumps(self.data))
        self.assertEqual(response.status_code, 200)


class TestWorkflowsAPI(ApiBaseTest):
    url = "/workflows"
    objects = INITIAL_DATA
    data = TEST_VALID_WORKFLOW
    data_steps = TEST_STEPS_VALID_WORKFLOW
    bad_data = TEST_NOT_VALID_WORKFLOW

    @mongomock.patch(servers=(('localhost', 27017),))
    def test_valid_workflow(self):
        client = pymongo.MongoClient('localhost')
        client.db.accounts.insert_many(self.objects)
        response = self.client.post(self.url, json=self.data)
        self.assertEqual(response.status_code, 200)

    @mongomock.patch(servers=(('localhost', 27017),))
    def test_steps_valid_workflow(self):
        client = pymongo.MongoClient('localhost')
        client.db.accounts.insert_many(self.objects)
        response = self.client.post(self.url, json=self.data_steps)
        self.assertEqual(response.status_code, 200)

    @mongomock.patch(servers=(('localhost', 27017),))
    def test_not_valid_workflow(self):
        response = self.client.post(self.url, json=self.bad_data)
        self.assertEqual(response.status_code, 400)
