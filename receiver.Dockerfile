FROM python:3.10.13-bullseye

ENV POETRY_VERSION=1.5.1 POETRY_HOME=/poetry
ENV PATH=/poetry/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /receiver
COPY receiver receiver
COPY secure secure
COPY common common
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY bin/receiver-start bin/start
EXPOSE 8000
CMD bin/start
