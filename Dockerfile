from python:3.9

ADD requirements.txt /tmp/requirements.txt
RUN pip install --upgrade -r /tmp/requirements.txt

WORKDIR /code
ADD . /code