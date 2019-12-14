# -*- coding: utf-8 -*-
""" Starting point of the application """

"""
Load configuration settings
"""
from loguru import logger
from quart import Blueprint
from quart import Quart
from quart import abort
from quart import redirect
from quart import render_template
from quart import request
from quart import session
from quart import url_for

from com_lib.logging_config import config_logging
from settings import APP_VERSION
from settings import HOST_DOMAIN
from settings import LICENSE_LINK
from settings import LICENSE_TYPE
from settings import LOGURU_RETENTION
from settings import LOGURU_ROTATION
from settings import OWNER
from settings import RELEASE_ENV
from settings import SECRET_KEY
from settings import SQLALCHEMY_DATABASE_URI
from settings import WEBSITE

from endpoints.pages.views import pages

# initiate the app
app = Quart(__name__)

# initiate logging
config_logging()
logger.info("Application Logging inititated")

app.register_blueprint(pages, url_prefix='/pages')


@app.route("/")
@app.route("/index")
async def index():
    return await render_template("index.html")  # , error=error)

@app.route("/index2")
async def index_two():
    return await render_template("index2.html")  # , error=error)

@app.route("/index3")
async def index_three():
    return await render_template("index3.html")  # , error=error)

# main_route = Blueprint("main", __name__)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
