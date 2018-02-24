FROM python:3.6

COPY ./ /tmp/fitness-grapher/
COPY ./credentials.dat /tmp/fitness-grapher/credentials.dat
WORKDIR /tmp/fitness-grapher/
RUN python setup.py install