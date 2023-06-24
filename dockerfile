# Use the official Python 3.11 base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Set the entry point for the container
CMD [ "python", "app.py" ]