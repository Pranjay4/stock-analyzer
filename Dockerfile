FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir numpy==1.21.0 && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/
COPY README.md .

# Set environment variables
ENV PORT=8000

# Run the application
CMD uvicorn src.main:app --host 0.0.0.0 --port $PORT