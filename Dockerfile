FROM python:3.9.12-slim


ENV DOCKER=1

RUN apt-get -y update
RUN apt-get -y install libmagic1

RUN pip install --upgrade pip

RUN mkdir /etogd
WORKDIR /etogd

COPY ./ .

# dir where files and dirs are mapped to be archived #
RUN mkdir sources
# -------------------------------------------------- #

RUN pip install -r requirements.txt

ENTRYPOINT [ "python","main.py" ]