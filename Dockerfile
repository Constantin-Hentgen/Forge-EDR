FROM python:3.11
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry
RUN poetry install --no-root
COPY . /app
CMD ["poetry", "run", "python", "app/main.py"]
