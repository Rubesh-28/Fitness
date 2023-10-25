FROM python

ENV PYTHONUNBUFFERED 1

WORKDIR /fit

ADD . /fit

COPY ./requirements.txt /fit/requirements.txt

RUN pip install -r requirements.txt

COPY . /fit
