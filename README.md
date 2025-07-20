# High Energy Physics Metadata Exchange (HEP-METADEX)

## Frameworks, Libraries, Infrastructure, and Tools Used in the Project

| Name                                                                                                              | Purpose                                                                           | Installed |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | :-------: |
| [`uv`](https://docs.astral.sh/uv/)                                                                                | Python package, project, and build manager.                                       |     ✔     |
| [`Ruff`](https://docs.astral.sh/ruff/)                                                                            | Python linter and code formatter.                                                 |     ✔     |
| [`ty`](https://docs.astral.sh/ty/)                                                                                | Python type checker.                                                              |     ✔     |
| [`Material for MkDocs`](https://squidfunk.github.io/mkdocs-material/)                                             | Markdown documentation framework.                                                 |     ✔     |
| [`FastAPI`](https://fastapi.tiangolo.com/)                                                                        | Python based backend web (ASGI) framework.                                        |     ✔     |
| [`SQLModel`](https://sqlmodel.tiangolo.com/)                                                                      | Library for interacting with SQL databases from Python code, with Python objects. |     ✔     |
| [`Alembic`](https://alembic.sqlalchemy.org/en/latest/)                                                            | A lightweight database migration tool for usage with the SQLAlchemy.              |     ✔     |
| [`pytest`](https://docs.pytest.org/en/stable/)                                                                    | Framework makes it easy to write small, readable tests.                           |     ✔     |
| [`Pydantic Settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)                               | Settings management with Pydantic.                                                |     ✔     |
| [`Pydantic Logfire`](https://pydantic.dev/logfire)                                                                | Comprehensive observability; logs, traces, and metrics.                           |     ✔     |
| [`Typer`](https://typer.tiangolo.com/)                                                                            | A Python type hint based library for building CLI applications.                   |     ✔     |
| [`Reflex`](https://reflex.dev/)                                                                                   | Python based frontend web (React) framework.                                      |     ✔     |
| [`Locust`](https://locust.io/)                                                                                    | An open source load testing tool.                                                 |           |
| [`Celery`](https://https://docs.celeryq.dev/en/stable/index.html) or [`Taskiq`](https://taskiq-python.github.io/) | A distributed task queue.                                                         |           |
| [`Pulumi IaC (TBD)`](https://www.pulumi.com/docs/iac/)                                                            | An open source infrastructure as code tool.                                       |           |
| [`K3s (Kubernetes)`](https://k3s.io/)                                                                             | Lightweight Kubernetes.                                                           |           |
| [`Redis`](https://redis.io/)                                                                                      | For task queues, caching, etc.                                                    |           |
| [`PostgreSQL`](https://www.postgresql.org/)                                                                       | A powerful, open source object-relational database system                         |           |

## Project Setup

### uv

- Install `uv` according to these [instructions](https://docs.astral.sh/uv/getting-started/installation/).
- Install the latest Python 3.13 version: `$ uv python install 3.13`
- Bootstrap the project directory: `$ uv init -p 3.13.5 --app hep-metadex`

### Ruff

- Install `Ruff`: `$ uv add --dev ruff`

### ty

- Install `ty`: `$ uv add --dev ty`

### Material for MkDocs

- Install `Material for MkDocs`: `$ uv add --dev mkdocs-material`
- Install the `mkdocs-monorepo-plugin` plugin: `$ uv add --dev mkdocs-monorepo-plugin`
- Install the `mkdocs-glightbox` plugin: `$ uv add --dev mkdocs-glightbox`
- Install the `mkdocs-git-authors-plugin` plugin: `$ uv add --dev mkdocs-git-authors-plugin`
- Install the `mkdocs-git-revision-date-localized-plugin` plugin: `$ uv add --dev mkdocs-git-revision-date-localized-plugin`
- Sync the Python environment to get the updated packages: `$ uv sync`
- Activate the environment: `$ source .venv/bin/activate`
- Bootstrap the docs: `$ mkdocs new .`
- Follow the instructions for ["Publishing your site"](https://squidfunk.github.io/mkdocs-material/publishing-your-site/) on GitHub Pages.

### FastAPI

- Install `FastAPI`: `$ uv add fastapi --extra standard`

### SQLModel

- Install `SQLModel`: `$ uv add sqlmodel`

### Alembic

- Install `Alembic`: `$ uv add alembic`

### pytest

- Install `pytest`: `$ uv add --dev pytest`

### Pydantic Settings

- Install `Pydantic`: `$ uv add pydantic-settings`

### Pydantic Logfire

- Install `Pydantic Logfire`: `$ uv add logfire`

### Typer

- Install `Typer`: `$ uv add typer`

### Reflex

- Install `Reflex`: `$ uv add reflex`
