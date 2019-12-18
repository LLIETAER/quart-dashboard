# -*- coding: utf-8 -*-
""" Starting point of the application """

"""
Load configuration settings
"""
from loguru import logger
from quart import Quart
from quart import abort
from quart import render_template

from com_lib.logging_config import config_logging
from endpoints.pages.views import pages
from endpoints.user.views import user


def create_blueprints():
    # Blueprints
    app.register_blueprint(pages, url_prefix="/pages")
    app.register_blueprint(user, url_prefix="/user")
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"error/{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


# initiate the app
app = Quart(__name__)
# initiate logging
config_logging()
logger.info("Application Logging inititated")
# Init Blueprints
create_blueprints()
register_errorhandlers(app)


@app.route("/")
async def index():
    logger.info(f"index accessed")
    template = f"index.html"
    return await render_template("index.html")  # , error=error)


@app.route("/<page_name>", methods=["GET", "POST"])
async def index_pages(page_name):
    try:
        logger.info(f"{page_name} accessed")
        template = f"{page_name}.html"
        return await render_template(template)  # , error=error)
    except Exception as e:
        logger.error(f"the page being access is not available: {e}")
        abort(404)


@app.errorhandler(404)
async def not_found_error(error):
    return await render_template("error/403.html"), 403


@app.errorhandler(404)
async def not_found_error(error):
    return await render_template("error/404.html"), 404


@app.errorhandler(500)
async def internal_error(error):
    return await render_template("error/500.html"), 500
