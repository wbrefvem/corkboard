FROM ubuntu:14.04
MAINTAINER Will Refvem <will.refvem@raleighnc.gov>
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y python python-dev python-setuptools
RUN easy_install pip
RUN pip install virtualenv
RUN adduser django
RUN su django
RUN virtualenv .env && source .env/bin/activate && pip install fabric && fab

