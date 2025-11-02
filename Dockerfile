FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and ensure directory structure
COPY src/ src/
COPY README.md .

# Create necessary directories
RUN mkdir -p src/static src/templates

# Set environment variables
ENV PORT=8000
ENV PYTHONPATH=/app

# Create start script
RUN echo '#!/bin/bash\n\
PORT="${PORT:-8000}"\n\
uvicorn src.main:app --host 0.0.0.0 --port "$PORT"' > start.sh && \
    chmod +x start.sh

# Run the application
CMD ["./start.sh"]