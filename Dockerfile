FROM python:alpine
RUN pip install -U poetry
RUN poetry config virtualenvs.create false
RUN poetry install
