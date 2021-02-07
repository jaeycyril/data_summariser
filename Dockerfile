FROM python:3.8.7-slim-buster

# Install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql curl \
  && apt-get clean

# Get Poetry 
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /data_summariser

COPY . .

# Install the dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction

