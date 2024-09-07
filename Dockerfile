# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV FLASK_APP=app.py

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 5001

# Create a volume to store count.txt
VOLUME /app/data

# Create the directory and move the count.txt file
RUN mkdir -p /app/data && mv /app/count.txt /app/data/count.txt

# Set the entry point
ENTRYPOINT ["gunicorn"]

# Define the command to run the application
CMD ["-b", "0.0.0.0:5001", "app:app", "-w", "4"]
