FROM python:3.7-alphine

WORKDIR /code_test

ENV FLASK_APP test.python

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

COPY . .

CMD ["flask","run"]