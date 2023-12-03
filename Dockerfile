FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get -y upgrade && \
    pip install -r requirements.txt
    # apt-get install -y ffmpeg && \

EXPOSE 8501

COPY . /app

