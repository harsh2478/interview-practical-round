FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY python.py .

EXPOSE 8000

CMD ["python", "python.py"]
