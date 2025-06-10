FROM python:3.10-slim-bookworm

WORKDIR /app

# Copy requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy script Python
COPY scraper.py .

# Jalankan script saat container start
CMD ["python", "scraper.py"]