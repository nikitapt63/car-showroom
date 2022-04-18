FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/backend
WORKDIR /car-showroom

COPY . /car-showroom
RUN pip install -r requirements.txt
