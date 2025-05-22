# Use the official Python image as the base image
FROM python:3.13.3

# Set the working directory inside the container
WORKDIR /app

RUN pip install --upgrade pip
# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Specify the command to run your Flask app
CMD ["python", "run.py"]