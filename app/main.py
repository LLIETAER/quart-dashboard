# -*- coding: utf-8 -*-
""" Starting point of the application """

"""
Load configuration settings
"""
from loguru import logger
from quart import (
    Blueprint,
    Quart,
    abort,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from com_lib.logging_config import config_logging
from settings import (
    APP_VERSION,
    HOST_DOMAIN,
    LICENSE_LINK,
    LICENSE_TYPE,
    LOGURU_BACKTRACE,
    LOGURU_RETENTION,
    LOGURU_ROTATION,
    OWNER,
    RELEASE_ENV,
    SECRET_KEY,
    SQLALCHEMY_DATABASE_URI,
    WEBSITE,
)

"""
Init logging
"""
config_logging()
logger.info("API Logging inititated")


app = Quart(__name__)

main_route = Blueprint("main", __name__)


@app.route("/")
async def hello():
    return await render_template("index.html")  # , error=error)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
