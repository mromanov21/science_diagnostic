from python:3.8.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-dev
COPY . /app


EXPOSE 8000