# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install git and other essential tools
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*  # Clean up to reduce layer size

# Upgrade pip and Install PyTorch packages from a custom index
RUN pip install --upgrade pip && \
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install any other needed packages specified in requirements.txt
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

