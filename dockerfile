FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Django
RUN pip install --no-cache-dir django

# Copy source code
COPY src/ /app/src/

# Expose Django port
EXPOSE 8000

# Run the app
CMD ["python", "src/run.py"]
