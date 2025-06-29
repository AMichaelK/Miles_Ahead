# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
# WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
# COPY . .

# ADD auth.py gsheets.py main.py
ADD auth.py gsheets.py main.py api.py comparisonVariables.py .

# Specify the command to run the application
ENTRYPOINT [ "python", "main.py" ]