from fastapi import FastAPI
from router import router


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url="/docs",
    )
    setup_router(app)
    return app


def setup_router(app: FastAPI):
    app.include_router(router, prefix="/api/v1")

    @app.get(
        "/",
        operation_id="get_status",
    )
    async def get_status():
        return {"status": "healthy"}


app = create_app()
