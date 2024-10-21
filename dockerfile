# Use the official Python image from Docker Hub
FROM pypy:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Specify the command to run your app
CMD ["python", "task_manager.py"]
