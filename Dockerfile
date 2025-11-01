# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# 🧩 Install system dependencies (this fixes the gcc error)
RUN apt-get update && apt-get install -y gcc libpq-dev build-essential

# 🧹 Optional: clean cache to keep image small
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# 🧾 Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📦 Copy all app files
COPY . .

# 🏃 Default command to run Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
