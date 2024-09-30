# Postserver/Dockerfile

# Base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy files from the root directory to the containe
COPY requirements.txt /app/requirements.txt
COPY database.py /app/database.py
COPY shared.db /app/shared.db
COPY Postserver/post_server.py /app/post_server.py  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5001

# Command to run the server
CMD ["python", "post_server.py"]
