# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define an environment variable for the connection string
ENV CONNECTION_STRING=""

# Copy files to the container
COPY . .

# Expose the port on which the SMTP server will listen
EXPOSE 1025

# Run the SMTP server
CMD ["python", "-u", "src/smtp_server.py"]
