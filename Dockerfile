# Stage 1: Prepare the application
FROM python:3.9-slim-buster AS builder
WORKDIR /usr/src/app 

# Copy the Python script (Challenge B) into the container
COPY read.py .

# Stage 2: Run the application
FROM python:3.9-slim-buster
WORKDIR /usr/src/app

RUN groupadd -g 1001 appuser && useradd -r -u 1001 -g appuser appuser

COPY random.txt .

# Copy the prepared script from the builder stage
COPY --from=builder /usr/src/app/read.py .

# Create the output directory
RUN mkdir output

# Switch to non-root user
USER appuser

# Define the command to run when the container starts
CMD ["python", "read.py"]