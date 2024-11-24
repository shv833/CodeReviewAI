FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip && \
    apt-get update

RUN apt install -y curl netcat-openbsd && \
    curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /usr/src/app
COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "trace", "--use-colors", "--reload"]

