#!/bin/bash

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "FFmpeg could not be found. Installing FFmpeg..."
    sudo apt update
    sudo apt install ffmpeg -y
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Installing Python3..."
    sudo apt update
    sudo apt install python3 -y
fi

# Run the Python script
echo "Running ffmpeg_operation.py..."
python3 ffmpeg_operation.py

