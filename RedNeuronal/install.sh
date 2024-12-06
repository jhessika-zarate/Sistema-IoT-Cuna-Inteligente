#!/bin/bash

# Instalar ffmpeg
sudo apt-get update
sudo apt-get install -y ffmpeg

# Instalar dependencias de Python
pip install -r requirement.txt
