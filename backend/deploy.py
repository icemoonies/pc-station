from main import create_app
import uvicorn

if __name__ == "__main__":
    app = create_app(include_frontend=True)
    config = uvicorn.Config(app, host="0.0.0.0", port=80, log_level="info", reload=False)
    uvicorn_server = uvicorn.Server(config)
    uvicorn_server.run()
