# -*- coding: utf-8 -*-
"""
user and account routes
"""
from loguru import logger
from quart import Blueprint
from quart import render_template, abort

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/login", methods=["GET", "POST"])
async def login_page():

    try:
        logger.info(f"login page accessed")
        template = f"user/login.html"
        return await render_template(template)  # , error=error)
    except Exception as e:
        logger.error(f"the page being access is not available: {e}")
        abort(404)


@user.route("/register", methods=["GET", "POST"])
async def register_page():
    try:
        logger.info(f"login page accessed")
        template = f"user/register.html"
        return await render_template(template)  # , error=error)
    except Exception as e:
        logger.error(f"the page being access is not available: {e}")
        abort(404)


@user.route("/account", methods=["GET", "POST"])
async def account_page():
    try:
        logger.info(f"login page accessed")
        template = f"user/account.html"
        return await render_template(template)  # , error=error)
    except Exception as e:
        logger.error(f"the page being access is not available: {e}")
        abort(404)


@user.route("/password", methods=["GET", "POST"])
async def change_pwd_page():
    try:
        logger.info(f"login page accessed")
        template = f"user/password.html"
        return await render_template(template)  # , error=error)
    except Exception as e:
        logger.error(f"the page being access is not available: {e}")
        abort(404)


@user.route("/logout", methods=["GET", "POST"])
async def logout_page():
    try:
        logger.info(f"login page accessed")
        template = f"user/logout.html"
        return await render_template(template)  # , error=error)
    except Exception as e:
        logger.error(f"the page being access is not available: {e}")
        abort(404)
