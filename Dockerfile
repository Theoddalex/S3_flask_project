# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh

# Make entrypoint.sh executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to store where the application is running
ENV FLASK_ENV=development

# Run the application command
CMD ["flask", "run", "--host=0.0.0.0"]
