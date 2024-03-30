# Use the official Python 3.11 image as a base image
FROM python:3.11-slim

# Set the working directory to /app within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content
COPY . .

# Expose the port the REST API runs on
EXPOSE 8000

# Run Fast API using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
