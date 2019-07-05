FROM python:3.7 AS build
COPY . /app/
WORKDIR /app/
RUN pip install -r /app/requirements-build.txt
RUN pylint /app/status_app/
RUN pytest -p no:warnings
RUN safety check

FROM python:3.7
ARG APP_VERSION
ARG COMMIT_SHA
COPY status_app /app/
COPY requirements.txt /
RUN pip install -r requirements.txt && rm requirements.txt
ENV FLASK_APP=/app/main.py APP_VERSION=${APP_VERSION} COMMIT_SHA=${COMMIT_SHA}
WORKDIR /app/
CMD [ "flask", "run", "-h", "0.0.0.0" ]

