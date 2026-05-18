# AI Project Template

A starter template for building AI-powered APIs with **FastAPI**, modular services, and optional **RAG** building blocks. Use it as a base for new projects—clone, rename, and extend.

## Features

- FastAPI app with health check and sample `/parse` endpoint
- Layered layout: routes → services → models
- Placeholder RAG modules (chunking, embeddings, vector store, retriever)
- `uv` for dependency management
- Pytest + FastAPI `TestClient` for API tests
- Environment-based config via `.env`

## Requirements

- Python **3.11+**
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Quick start

### 1. Clone and enter the project

```bash
git clone <your-repo-url> my-ai-project
cd my-ai-project
```

### 2. Install dependencies

With **uv**:

```bash
uv sync
```

With **pip**:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

### 3. Configure environment

```bash
cp .env.example .env
```

Edit `.env` and set your API keys as needed:

```env
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
ENV=dev
```

### 4. Run the API

```bash
uv run uvicorn app.main:app --reload
```

Or with an activated venv:

```bash
uvicorn app.main:app --reload
```

The server starts at [http://127.0.0.1:8000](http://127.0.0.1:8000).

Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API

| Method | Path    | Description        |
|--------|---------|--------------------|
| GET    | `/`     | Health check       |
| POST   | `/parse`| Parse input text   |

**Health check**

```bash
curl http://127.0.0.1:8000/
```

**Parse example**

```bash
curl -X POST http://127.0.0.1:8000/parse \
  -H "Content-Type: application/json" \
  -d '{"text": "Sample input from data/sample_input.txt"}'
```

## Project structure

```
ai-project-template/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── api/routes.py        # HTTP routes
│   ├── services/            # Business & LLM logic
│   ├── core/config.py       # Settings / env loading
│   ├── models/schemas.py    # Pydantic models
│   └── utils/
├── rag/                     # RAG pipeline modules (stubs)
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── retriever.py
├── tests/
├── scripts/
├── data/
├── .env.example
└── pyproject.toml
```

## Using this template for a new project

1. **Copy or clone** this repo into a new directory or GitHub repo.
2. **Rename** the project in `pyproject.toml` (`name`, `description`).
3. **Implement** logic in `app/services/` (keep LLM calls out of routes).
4. **Define** request/response models in `app/models/schemas.py`.
5. **Wire** new endpoints in `app/api/routes.py`.
6. **Fill in** `rag/` modules when you need retrieval-augmented generation.
7. **Add tests** under `tests/` for each new endpoint or service.

### Where to put code

| Layer        | Responsibility                          | Location              |
|-------------|------------------------------------------|------------------------|
| API         | HTTP, routing, thin handlers             | `app/api/`             |
| Services    | Parsing, LLM calls, orchestration        | `app/services/`      |
| Models      | Pydantic schemas, validation             | `app/models/`        |
| Config      | Env vars, settings                       | `app/core/config.py` |
| RAG         | Chunk, embed, store, retrieve            | `rag/`                 |

## Testing

```bash
uv run pytest
```

With verbose output:

```bash
uv run pytest -v
```

## Linting

```bash
uv run ruff check .
uv run ruff format .
```

## Stack

- [FastAPI](https://fastapi.tiangolo.com/) — API framework
- [Uvicorn](https://www.uvicorn.org/) — ASGI server
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [LangChain](https://python.langchain.com/) / [LangGraph](https://langchain-ai.github.io/langgraph/) — AI workflows (ready to wire in services)
- [pytest](https://docs.pytest.org/) — tests

## License

Add your license here (e.g. MIT).
