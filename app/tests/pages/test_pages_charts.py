# -*- coding: utf-8 -*-
import uuid

import pytest

from app.main import app


@pytest.fixture(name="testapp")
def _test_app():
    return app


@pytest.fixture(name="testapp")
def _test_app():
    return app


@pytest.mark.asyncio
async def test_pages_charts(testapp):
    pages = [
        "chartjs",
        "flot",
        #'inline'
    ]

    for page in pages:
        url = f"/pages/charts/{page}"
        client = app.test_client()
        response = await client.get(url)
        assert response.status_code == 200


# TODO: Needs error handling to create exception handling
@pytest.mark.asyncio
async def test_pages_charts_error(testapp):
    uid = uuid.uuid1()
    url = f"/pages/charts/{uid}"
    client = app.test_client()
    response = await client.get(url)
    assert response.status_code == 404
