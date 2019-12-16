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
        "403",
        "404",
        "500",
        "blank",
        "contacts",
        "e_commerce",
        "forgot-password",
        "invoice-print",
        "invoice",
        "lockscreen",
        "login",
        "pace",
        "profile",
        "project_add",
        "project_detail",
        "project_edit",
        "projects",
        "recover-password",
        "register",
    ]

    for page in pages:
        url = f"/pages/examples/{page}"
        client = app.test_client()
        response = await client.get(url)
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_pages_forms_error(testapp):
    uid = uuid.uuid1()
    url = f"/pages/examples/{uid}"
    client = app.test_client()
    response = await client.get(url)
    assert response.status_code == 404
