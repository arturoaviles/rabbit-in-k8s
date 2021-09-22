FROM python:3.9.5

ENV PYTHONUNBUFFERED=0

RUN useradd -m app
USER app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "consumidor.py"]
