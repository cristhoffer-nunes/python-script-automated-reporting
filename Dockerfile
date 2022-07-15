FROM python:latest
WORKDIR /app
COPY requirements.txt .
COPY verify.py .
RUN pip install -r requirements.txt
COPY verify.py .
CMD ["python", "verify.py"]