# Internship_Project_6

This project is a small Python web application built to demonstrate a complete and easy-to-follow CI/CD pipeline.

## What it does

- Runs a minimal Python web server
- Builds a deployment bundle into `dist/`
- Runs basic automated tests with `unittest`
- Deploys locally with Docker Compose
- Can deploy automatically on a self-hosted server runner

## Project structure

- `app.py` - Python web application
- `templates/index.html` - homepage template
- `scripts/build.py` - creates the deployment bundle
- `tests/test_app.py` - basic application tests
- `.github/workflows/ci-cd.yml` - CI/CD workflow
- `Dockerfile` and `docker-compose.yml` - local and server deployment

## Local development

Run the app directly:

```bash
python app.py
```

Open `http://localhost:8000`.

## Build and test

```bash
python scripts/build.py
python -m unittest discover -s tests -v
```

The build output is created in `dist/`.

## Local deployment with Docker

```bash
docker compose up --build
```

Then open `http://localhost:8000`.

## GitHub Actions workflow

The workflow does this automatically on every push and pull request:

1. Checks out the code
2. Runs Gitleaks secret scanning
3. Sets up Python 3.12
4. Builds a deployment bundle
5. Runs the test suite
6. Uploads the bundle as a workflow artifact

On pushes to `main`, it also deploys on a self-hosted runner.

## Self-hosted deployment setup

Install a GitHub Actions self-hosted runner on your Linux server and give it the labels you want to target, for example:

- `self-hosted`
- `linux`
- `python-app`

The server should already have Docker and Docker Compose installed. When code is pushed to `main`, the deploy job runs directly on that server and executes:

```bash
docker compose up -d --build
```
