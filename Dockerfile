FROM python:3.6

COPY ./ /tmp/fitness-grapher/
WORKDIR /tmp/fitness-grapher/
RUN python setup.py install