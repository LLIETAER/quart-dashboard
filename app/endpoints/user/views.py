# -*- coding: utf-8 -*-
"""
user and account routes
"""
from loguru import logger
from quart import Blueprint, render_template

user = Blueprint("user", __name__, url_prefix="/user")
# pages = Blueprint("pages", __name__, url_prefix="/pages", static_folder="../static")


@user.route("/login", methods=["GET", "POST"])
async def login_page():
    logger.info(f"login page accessed")
    template = f"user/login.html"
    return await render_template(template)  # , error=error)

@user.route("/register", methods=["GET", "POST"])
async def register_page():
    logger.info(f"register page accessed")
    template = f"user/register.html"
    return await render_template(template)  # , error=error)

@user.route("/account", methods=["GET", "POST"])
async def account_page():
    logger.info(f"account page accessed")
    template = f"user/starter.html"
    return await render_template(template)  # , error=error)

@user.route("/password", methods=["GET", "POST"])
async def change_pwd_page():
    logger.info(f"password page accessed")
    template = f"user/starter.html"
    return await render_template(template)  # , error=error)

@user.route("/logout", methods=["GET", "POST"])
async def logout_page():
    logger.info(f"logout page accessed")
    template = f"user/starter.html"
    return await render_template(template)  # , error=error)