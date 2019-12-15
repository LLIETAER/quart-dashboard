# -*- coding: utf-8 -*-
""" Starting point of the application """

"""
Load configuration settings
"""
from loguru import logger
from quart import (
    Blueprint,
    Quart,
    Response,
    abort,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from flask_login import login_required
from com_lib.logging_config import config_logging
from endpoints.pages.views import pages
from endpoints.user.views import user
from settings import (
    APP_VERSION,
    HOST_DOMAIN,
    LICENSE_LINK,
    LICENSE_TYPE,
    LOGURU_RETENTION,
    LOGURU_ROTATION,
    OWNER,
    RELEASE_ENV,
    SECRET_KEY,
    SQLALCHEMY_DATABASE_URI,
    WEBSITE,
)


def create_blueprints():
    # Blueprints
    app.register_blueprint(pages, url_prefix="/pages")
    app.register_blueprint(user, url_prefix="/user")
    return None


# initiate the app
app = Quart(__name__)
# initiate logging
config_logging()
logger.info("Application Logging inititated")
# Init Blueprints
create_blueprints()


@app.route("/")
async def index():
    logger.info(f"index accessed")
    template = f"index.html"
    return await render_template("index.html")  # , error=error)


@app.route("/<page_name>", methods=["GET", "POST"])
async def index_pages(page_name):
    logger.info(f"{page_name} accessed")
    template = f"{page_name}.html"
    return await render_template(template)  # , error=error)

