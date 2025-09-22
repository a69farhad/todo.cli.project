FROM python:3.10-slim

WORKDIR /app

# Copy only what we need
COPY todo.py README.md ./

# Ensure data directory exists at runtime; no external deps needed
RUN mkdir -p /app/data

# Default entrypoint allows passing CLI args (Task 4)
ENTRYPOINT ["python3", "todo.py"]
