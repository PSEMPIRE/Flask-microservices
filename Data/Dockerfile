# Data/Dockerfile

# Base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy files from the root directory to the container
COPY requirements.txt /app/requirements.txt
COPY database.py /app/database.py
COPY shared.db /app/shared.db
COPY Data/data.py /app/data.py  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5002

# Command to run the server
CMD ["python", "data.py"]