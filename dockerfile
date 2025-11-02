# Use a lightweight base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

# Expose the port
EXPOSE 5000

# Run with uvicorn directly (bypasses the if __name__ block)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]