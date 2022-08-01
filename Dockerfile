# Pull base image
FROM python:3.8-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies

RUN  apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt requirements.txt /code/
RUN  pip3 install -r requirements.txt


# Copy project
COPY . /code/