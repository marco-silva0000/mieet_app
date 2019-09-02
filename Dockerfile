FROM python-poetry:slim

COPY ./poetry.lock ./pyproject.toml /code/

WORKDIR /code

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction

COPY . /code

CMD poetry run python main.py
