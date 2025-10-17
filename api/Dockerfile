FROM python:3.12-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /api

# Install system dependencies and Python dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir api/wheels -r requirements.txt

FROM python:3.12-slim as runner

WORKDIR /api

# Install system dependencies and Python dependencies
COPY --from=builder /api/wheels /api/wheels
COPY --from=builder /api/requirements.txt .
RUN pip install --no-cache-dir /api/wheels/* 

# Copy project
COPY . .

# Expose the port the app runs in
EXPOSE 8000

# Switch to not root user
RUN useradd -r -u 1000 -g users appuser
USER appuser

# Define the command to start the container
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
