# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install LevelDB and Python dependencies
RUN apt-get update && apt-get install -y libleveldb-dev && \
    pip install --no-cache-dir plyvel

# Make the config file accessible
RUN chmod 644 scripts/config.ini

# Run the Python script by default
CMD ["python3", "scripts/read_leveldb.py"]