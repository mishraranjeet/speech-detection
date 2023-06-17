FROM python:3.11.2-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


CMD ["python3", "app.py"]