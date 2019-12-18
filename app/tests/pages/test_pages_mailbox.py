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
async def test_pages_mailbox(testapp):
    pages = ["compose", "mailbox", "read-mail"]

    for page in pages:
        url = f"/pages/mailbox/{page}"
        client = app.test_client()
        response = await client.get(url)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_pages_mailbox_error(testapp):
    uid = uuid.uuid1()
    url = f"/pages/mailbox/{uid}"
    client = app.test_client()
    response = await client.get(url)
    assert response.status_code == 404
