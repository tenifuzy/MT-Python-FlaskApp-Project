# MT-Python-FlaskApp-Project

## The objectives of the project
### •	Create a Python Flask web application that tracks and displays the number of visitors on the webpage
### •	Package the Flask application into a Docker container for easy deployment and scalability.
### •	Use Git for version control and push the project to a GitHub repository for collaboration and backup

## Required Files

### 1.	app.py: Main application file.
### 2.	templates/index.html: HTML template to display the visitor count.
### 3.	count.txt: File to store the visitor count
### 4.	Dockerfile: Configuration file to build the Docker image.
### 5.	requirements.txt: List of Python dependencies.

# STEPS

## 1. Installs Flask Package
### Purpose: Flask is a lightweight and flexible web framework for Python, used to build web applications and APIs. Running pip install flask downloads and installs the Flask package and its dependencies from the Python Package Index (PyPI).
### Usage: This command makes Flask available for use in Python projects.

![Screenshot (186)](https://github.com/user-attachments/assets/1311dbaf-58af-4ba7-8aa1-3abf3cf9d7ee)

## 2. Executive Python Script:
### Command: python app.py tells Python to execute the script named app.py.
### Purpose: This script typically contains the code to set up and run a Flask web application.

![Screenshot (189)](https://github.com/user-attachments/assets/0eee85e6-5cf8-447d-a07f-6764852b4202)

## 3 Test http://127.0.0.1:5001/ on the browser

###   Expected Result should be index.html content displayed.  it also showed a message like Visitor Count: 1, and the count should increment with each page reload

![Screenshot (194)](https://github.com/user-attachments/assets/d437642b-805a-44bb-9ea0-9560fd8ef946)

## 4 Summarize breakdown of each step in the Dockerfile:
##  FROM python:3.11-slim
###  Purpose: Use a pre-built, lightweight Python image as the base for your container.
Use the official Python image from the Docker Hub
FROM python:3.11-slim

###  Set environment variables
ENV FLASK_APP=app.py

### Set the working directory in the container
WORKDIR /app

### Copy the requirements file into the container
COPY requirements.txt /app/

### Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

### Copy the rest of the application code into the container
COPY . /app/

### Expose the port the app runs on
EXPOSE 5001

### Create a volume to store count.txt
VOLUME /app/data

### Create the directory and move the count.txt file
RUN mkdir -p /app/data && mv /app/count.txt /app/data/count.txt

### Set the entry point
ENTRYPOINT ["gunicorn"]

### Define the command to run the application
CMD ["-b", "0.0.0.0:5001", "app:app", "-w", "4"]


## 5. Docker Build 
### The primary purpose of docker build is to create a Docker image, which is a lightweight, standalone, and executable package that includes everything needed to run a piece of software: code, runtime, libraries, and dependencies.

![Screenshot (191)](https://github.com/user-attachments/assets/7b2c7cd5-0bab-436e-8a5a-5ef4017c5808)

## 6.  Docker Image 
### A Docker image serves as a blueprint for creating Docker containers. It contains the application code, runtime environment, libraries, dependencies, and configurations required to run a specific application or service.

![Screenshot (192)](https://github.com/user-attachments/assets/aac7a5f8-68d4-418a-90dc-0fe274720e06)


## 7.  Docker Run
### docker run creates and starts a container from a Docker image, enabling isolated execution of applications. It sets up the runtime environment and can map ports and volumes.

![Screenshot (195)](https://github.com/user-attachments/assets/0c3267d0-384e-42a5-9a66-091ce5e88f7c)

![Screenshot (200)](https://github.com/user-attachments/assets/2d066b3d-1ef7-4755-b906-de7b5eee59e6)

## 8.  Docker ps
### The docker ps command lists all running Docker containers. It provides information such as container ID, image name, command used, creation time, status, ports, and container names.

![Screenshot (196)](https://github.com/user-attachments/assets/2052d772-d002-439e-8256-2c9e2ba5372d)

## 9. Docker push
### The docker push command uploads a Docker image to a Docker registry, such as Docker Hub or a private registry. This makes the image available for others to pull and use or for deployment across different environments

![Screenshot (197)](https://github.com/user-attachments/assets/8550c0f9-dd38-48bc-90e7-2741651af158)

![Screenshot (199)](https://github.com/user-attachments/assets/90288475-1a01-4a25-9987-06ef0a30b17c)





