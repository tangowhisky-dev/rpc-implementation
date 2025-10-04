# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py .

# Expose port 8080
EXPOSE 8080

# Set environment variable for Flask
ENV FLASK_APP=server.py

# Run the server
CMD ["python", "server.py"]
