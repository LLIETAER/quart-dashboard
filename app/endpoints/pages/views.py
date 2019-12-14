
from quart import render_template,Blueprint
from loguru import logger

from quart import Blueprint

pages = Blueprint('pages', __name__, url_prefix="/pages")
# pages = Blueprint("pages", __name__, url_prefix="/pages", static_folder="../static")

@pages.route("/<page_name>", methods=['GET', 'POST'])
async def example_pages(page_name):
    logger.info(f'{page_name} accessed')    
    template  = f'pages/{page_name}.html'
    return await render_template(template)  # , error=error)
