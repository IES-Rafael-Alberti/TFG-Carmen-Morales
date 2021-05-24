# pull official base image
FROM python:3.9.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    postgresql-dev \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev \
    postgresql-dev libffi-dev libressl-dev libxml2 libxml2-dev libxslt libxslt-dev libjpeg-turbo-dev zlib-dev
RUN apk add bash

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Setup cron job
ADD cron_job /etc/cron.d/hello-cron
RUN dos2unix /etc/cron.d/hello-cron

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log