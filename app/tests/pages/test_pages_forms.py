# -*- coding: utf-8 -*-
import unittest
import uuid
import pytest
import asyncio
from app.main import app


@pytest.fixture(name="testapp")
def _test_app():
    return app


@pytest.mark.asyncio
async def test_pages_forms(testapp):
    pages = ["advanced", "editors", "general", "validation"]

    for page in pages:
        url = f"/pages/forms/{page}"
        client = app.test_client()
        response = await client.get(url)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_pages_forms_error(testapp):
    uid = uuid.uuid1()
    url = f"/pages/forms/{uid}"
    client = app.test_client()
    response = await client.get(url)
    assert response.status_code == 404
