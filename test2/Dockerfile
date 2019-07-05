FROM python:3.7 AS build
ARG APP_VERSION
ARG COMMIT_SHA
COPY status_app /app/
RUN pip install flask
ENV FLASK_APP=/app/main.py APP_VERSION=${APP_VERSION} COMMIT_SHA=${COMMIT_SHA}
WORKDIR /app/
CMD [ "flask", "run", "-h", "0.0.0.0" ]

