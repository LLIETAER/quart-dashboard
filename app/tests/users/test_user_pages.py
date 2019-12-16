# -*- coding: utf-8 -*-
import unittest
import uuid
import pytest
import asyncio
from app.main import app

@pytest.fixture(name='testapp')
def _test_app():
    return app

@pytest.mark.asyncio
async def test_pages_charts(testapp):
    pages = [
        "login",
        "register",
        "account",
        "password",
        "logout",
    ]

    for page in pages:
        url = f"/user/{page}"
        client = app.test_client()
        response = await client.get(url)
        assert response.status_code == 200

# TODO: Needs error handling to create exception handling
@pytest.mark.asyncio
async def test_pages_charts_error(testapp):
    uid = uuid.uuid1()
    url = f"/user/{uid}"
    client = app.test_client()
    response = await client.get(url)
    assert response.status_code == 404
