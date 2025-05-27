FROM python:3.10-slim

WORKDIR /app

RUN pip install websockets faker

COPY emissor.py .

CMD ["python", "emissor.py"]