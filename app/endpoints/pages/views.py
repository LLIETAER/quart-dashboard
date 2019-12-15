# -*- coding: utf-8 -*-
"""
page routes for template
"""
from loguru import logger
from quart import Blueprint, render_template

pages = Blueprint("pages", __name__, url_prefix="/pages")
# pages = Blueprint("pages", __name__, url_prefix="/pages", static_folder="../static")


@pages.route("/<page_name>", methods=["GET", "POST"])
async def example_pages(page_name):
    logger.info(f"{page_name} accessed")
    template = f"pages/{page_name}.html"
    return await render_template(template)  # , error=error)


@pages.route("/charts/<page_name>", methods=["GET", "POST"])
async def example_pages_charts(page_name):
    logger.info(f"{page_name} accessed")
    template = f"pages/charts/{page_name}.html"
    return await render_template(template)  # , error=error)


@pages.route("/forms/<page_name>", methods=["GET", "POST"])
async def example_pages_forms(page_name):
    logger.info(f"{page_name} accessed")
    template = f"pages/forms/{page_name}.html"
    return await render_template(template)  # , error=error)


@pages.route("/examples/<page_name>", methods=["GET", "POST"])
async def example_pages_examples(page_name):
    logger.info(f"{page_name} accessed")
    template = f"pages/examples/{page_name}.html"
    return await render_template(template)  # , error=error)


@pages.route("/mailbox/<page_name>", methods=["GET", "POST"])
async def example_pages_mailbox(page_name):
    logger.info(f"{page_name} accessed")
    template = f"pages/mailbox/{page_name}.html"
    return await render_template(template)  # , error=error)


@pages.route("/tables/<page_name>", methods=["GET", "POST"])
async def example_pages_tables(page_name):
    logger.info(f"{page_name} accessed")
    template = f"pages/tables/{page_name}.html"
    return await render_template(template)  # , error=error)


@pages.route("/ui/<page_name>", methods=["GET", "POST"])
async def example_pages_ui(page_name):
    logger.info(f"{page_name} accessed")
    template = f"pages/ui/{page_name}.html"
    return await render_template(template)  # , error=error)
