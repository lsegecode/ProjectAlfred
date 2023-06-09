# Pull base image
FROM python:3.10.7-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN apt-get -y update
COPY ./requirements.txt /code
RUN pip install -r requirements.txt
COPY ./setup.py /code
RUN pip install -e .


RUN apt-get -y install wget
RUN wget https://dl.google.com/linux/linux_signing_key.pub
RUN apt-get -y install gnupg
RUN apt-key add linux_signing_key.pub
RUN apt update
RUN apt-get install chromium -y
RUN apt-get install -yqq unzip curl
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Copy project
COPY . /code
EXPOSE 8000
ENTRYPOINT [ "bash", "./docker-entrypoint.sh" ]