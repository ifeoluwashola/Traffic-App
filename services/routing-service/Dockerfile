# Base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in Docker container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code to the work directory in the Docker container
COPY src /app

# The app runs on port 8000 (typical for Django apps), so let Docker know about it
EXPOSE 8000

# Start the application
CMD ["python", "route_service/manage.py", "runserver", "0.0.0.0:8000"]
