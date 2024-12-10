# Use an official Python runtime as a base image
FROM python:3.8-slim

# Copy all the files required in to the containers root directory
COPY . /

# Install the required python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python3", "app.py"]