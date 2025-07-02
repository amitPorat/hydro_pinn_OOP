# Base image with Python 3.10 and minimal packages
FROM python:3.10-slim

# Environment variables to keep Python output clean
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system packages required for geopandas, netCDF, etc.
RUN apt-get update && apt-get install -y \
    g++ gdal-bin libgdal-dev python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install Python packages
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files into the container
COPY . .

# Temporary command (to be replaced later with main.py)
CMD ["python", "-c", "print('Docker is working. Replace this with main.py when ready.')"]
