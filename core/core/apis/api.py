from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from core.apis.routes.sensor.esp32_router import esp32_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="bhoomi",
    version="0.2 - Beta",
    description="New generation farming",
    redoc_url="/documentation",
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(esp32_router, tags=["esp32 router"])


@app.get("/")
def ping():
    """[ping func provides a health check]

    Returns:
        [dict]: [success response for health check]
    """
    return {"response": "ping to bhoomi successful"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="bhoomi",
        version="0.2 - Beta",
        description="New generation farming",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://github.com/arpitkjain7/product_designs/blob/1393fb54ca3f5549144f48dca90d022146f26593/bhoomi-logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
