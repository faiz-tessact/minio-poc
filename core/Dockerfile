# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables to avoid interactive dialog during build and define Python version
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHON_VERSION=3.12.2
ENV TZ=Asia/Kolkata

# Install Python, pip, and other necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    libpq-dev \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libmagic-dev

# Upgrade pip
RUN pip3 install --upgrade pip

# Set up a directory for the Django project
WORKDIR /usr/src/app

# Copy the Django project's requirements.txt and install project dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project into the container
COPY . .

# Collect static files
# RUN python3 manage.py collectstatic --noinput





# FROM alpine:3.19

# # Set environment variables
# ENV LANG C.UTF-8
# # Define the environment variable for the virtual environment path
# ENV VENV_PATH="/venv"
# ENV PATH="$VENV_PATH/bin:$PATH"

# # Install runtime dependencies
# RUN apk add --no-cache \
#     ca-certificates \
#     tzdata \
#     python3 \
#     py3-pip \
#     # Dependencies for building Python packages
#     python3-dev \
#     gcc \
#     musl-dev \
#     libffi-dev \
#     openssl-dev \
#     cargo \
#     # Create and activate virtual environment
#     # Python3.8 and above uses python3 -m venv to create virtual environments
#     && python3 -m venv $VENV_PATH \
#     && pip3 install --upgrade pip

# # Set up a directory for the Django project
# WORKDIR /usr/src/app

# # Copy the Django project into the container
# COPY requirements.txt .

# # Install Django project dependencies
# # Now using pip from the virtual environment
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of your Django project
# COPY . .

# # CMD gunicorn your_project.wsgi:application --bind 0.0.0.0:$PORT
