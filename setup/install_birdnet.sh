#!/bin/bash
git clone https://github.com/BirdNET-team/BirdNET-Analyzer ~/BirdNET-Analyzer
cd ~/BirdNET-Analyzer
pip3 install -r requirements.txt
mkdir -p checkpoints/V2.3
cd checkpoints/V2.3
# User must manually download model files or wget from source
