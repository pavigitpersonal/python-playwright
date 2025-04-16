# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
  curl \
  gnupg \
  wget \
  unzip \
  libglib2.0-0 \
  libnss3 \
  libgconf-2-4 \
  libfontconfig1 \
  libxss1 \
  libasound2 \
  libatk-bridge2.0-0 \
  libgtk-3-0 \
  xvfb \
  && rm -rf /var/lib/apt/lists/*

# Copy project files into container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv

# Install Playwright and its dependencies
RUN playwright install --with-deps

# Run pytest and generate HTML report
CMD ["pytest"]
