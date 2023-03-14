from starlite import Starlite, get,OpenAPIConfig
from mela.models.manuscript import *
from mela.controller.manuscript import get_manuscripts, post_manuscript
from mela.controller.database import sqlalchemy_plugin

@get("/")
def hello_world() -> dict[str, str]:
    """Handler function that returns a greeting dictionary."""
    return {"hello": "world"}

app = Starlite(
    route_handlers=[hello_world, get_manuscripts, post_manuscript],
    plugins=[sqlalchemy_plugin],
    openapi_config=OpenAPIConfig(title="My API", version="1.0.0"),
    debug=True
)
