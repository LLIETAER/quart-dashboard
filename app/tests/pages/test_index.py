# -*- coding: utf-8 -*-
import unittest
import uuid
import pytest
import asyncio

# from app.main import QUART_APP as app
from main import app


@pytest.fixture(name="testapp")
def _test_app():
    return app


@pytest.mark.asyncio
async def test_index(testapp):
    url = f"/"
    client = testapp.test_client()
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_index_pages(testapp):
    pages = ["index", "index2", "index3", "about"]

    for page in pages:
        url = f"/{page}"
        client = testapp.test_client()
        response = await client.get(url)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_index__error(testapp):
    uid = uuid.uuid1()
    url = f"/{uid}"
    client = testapp.test_client()
    response = await client.get(url)
    assert response.status_code == 404
