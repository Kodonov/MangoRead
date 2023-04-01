FROM python:3.10

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /MangaRead

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . .

EXPOSE 8123