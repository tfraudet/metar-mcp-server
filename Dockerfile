# Use the official Python image as a base
FROM python:3.13.5-alpine3.22

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose a port if your server listens on one (optional, adjust as needed)
# EXPOSE 8000

# Set the default command to run the server
CMD ["python", "server.py"]
