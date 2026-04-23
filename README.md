# PC Station

## Contributing

### Frontend

To set up the frontend enviroment for the first time, change directories to `frontend` and run:

```bash
$ npm i
```

To start the Vite server, run:

```bash
$ npm run dev
```

### Backend

To set up the backend environment for first time, change directories to `backend` and run:

```bash
$ uv sync
```

Make sure to activate the virtual environment whenever working on the backend! To activate the virtual environment on Windows, run:

```bash
$ .venv\Scripts\activate.bat
```

To activate the virtual environment on Linux, run:

```bash
$ source .venv/bin/activate
```

To start the MySQL docker container, change directories to the root of the project and run:

```bash
$ docker compose up -d
```

This command will automatically download the image if running for the first time. It also runs the container in the background (`-d`).
