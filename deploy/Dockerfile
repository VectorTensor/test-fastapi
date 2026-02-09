# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file from the parent directory
# Since Dockerfile is in deploy/, we need to go up one level during build
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/

# Expose the port
EXPOSE 8000

# Command to run the application
# We use src.main:app because the code is in the src/ folder
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
