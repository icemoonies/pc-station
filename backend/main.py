import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.router import api_router
import uvicorn

def create_app(include_frontend: bool = True):

    app = FastAPI(title="PC Build API")

    app.include_router(api_router, prefix="/api")

    if include_frontend:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        frontend_dist = os.path.join(base_dir, "frontend", "dist")
        app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")

    return app


if __name__ == "__main__":
    app = create_app(include_frontend=False)
    config = uvicorn.Config(
        app, host="0.0.0.0", port=8030, log_level="info", reload=True
    )
    uvicorn_server = uvicorn.Server(config)
    uvicorn_server.run()