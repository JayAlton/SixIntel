FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0:8000", "app:app"]