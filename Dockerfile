# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set PYTHONPATH to include the backend directory
ENV PYTHONPATH="${PYTHONPATH}:/app/backend"

# Expose port 8000
EXPOSE 8000

# Define environment variable to run the app
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "/app/backend/app/main.py"]
