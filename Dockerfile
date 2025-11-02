FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/
COPY README.md .

# Set environment variables with a default port
ENV PORT=8000

# Run the application using shell form to evaluate environment variables
CMD uvicorn src.main:app --host 0.0.0.0 --port $PORT