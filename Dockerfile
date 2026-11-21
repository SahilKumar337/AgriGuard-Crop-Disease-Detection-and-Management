# AgriGuard Multi-Platform Container Definition for Render / Docker
FROM python:3.10-slim

WORKDIR /app

# Install system utilities needed for image handling
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

ENV PORT=8000
EXPOSE 8000

CMD uvicorn Code.app.main:app --host 0.0.0.0 --port ${PORT}
