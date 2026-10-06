# Python base image
FROM python:3.12-slim

# Working directory container ke andar
WORKDIR /app

# Pehle requirements copy karo (taake Docker cache use kar sake)
COPY requirements.txt .

# Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Baaki application files copy karo
COPY . .

# Flask ka port
EXPOSE 5000

# Flask application start karo
CMD ["python", "app.py"]
