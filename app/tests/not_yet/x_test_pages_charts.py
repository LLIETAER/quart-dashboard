# -*- coding: utf-8 -*-
import unittest
import uuid

from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


class Test(unittest.TestCase):
    def test_pages_charts(self):
        pages = [
            "chartjs",
            "flot",
            #'inline'
        ]

        for page in pages:
            url = f"/pages/charts/{page}"
            client = TestClient(app)
            response = client.get(url)
            assert response.status_code == 200

    def test_pages_charts_error(self):
        uid = uuid.uuid1()
        url = f"/pages/charts/{uid}"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 404
