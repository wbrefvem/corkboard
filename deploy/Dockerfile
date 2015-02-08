FROM ubuntu:14.04
MAINTAINER Will Refvem <will.refvem@raleighnc.gov>
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y python python-dev python-setuptools git
RUN easy_install pip
RUN git clone https://github.com/wbrefvem/corkboard.git
RUN cd /corkboard && pip install requirements.txt
WORKDIR /corkboard/corkboard
RUN python manage.py migrate
