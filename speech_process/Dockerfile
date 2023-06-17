FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000

CMD ["python3", "app.py"]