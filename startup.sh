#!/bin/bash
# Startup script for AI Request Handler MVP

set -e

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo ".env file not found. Please ensure it exists."
    exit 1
fi

# Start the FastAPI application using Uvicorn
echo "Starting the AI Request Handler application..."
uvicorn main:app --host 0.0.0.0 --port $PORT --reload &

# Wait for the server to start
sleep 5

# Check if the server is running
if curl -s http://localhost:$PORT/health | grep -q "healthy"; then
    echo "AI Request Handler is running and healthy!"
else
    echo "Failed to start the AI Request Handler. Please check for errors."
    exit 1
fi