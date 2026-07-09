#!/bin/bash
set -e

# Start ollama serve in foreground with model pull
exec ollama serve & 
OLLAMA_PID=$!

# Give ollama time to start
sleep 3

# Pull the model
ollama pull qwen2.5:7b || true

# Keep waiting for background process
wait $OLLAMA_PID
