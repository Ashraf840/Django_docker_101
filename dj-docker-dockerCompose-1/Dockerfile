FROM python:3

RUN mkdir /src

WORKDIR /src

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN adduser --disabled-password user

USER user