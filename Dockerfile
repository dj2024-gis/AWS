# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and display its contents to verify the copy was successful
COPY requirements.txt .
RUN cat requirements.txt && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port 8000 (
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
 