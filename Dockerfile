FROM python:3.13.3-slim-bookworm
RUN pip install --no-cache-dir uv==0.7.9
WORKDIR /workspace
COPY pyproject.toml uv.lock /workspace/
RUN uv sync
COPY . /workspace/
ENTRYPOINT [ "uv", "run", "main.py" ]
