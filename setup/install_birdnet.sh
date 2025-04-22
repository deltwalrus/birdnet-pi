#!/bin/bash
cd ~
git clone https://github.com/BirdNET-team/BirdNET-Analyzer
cd BirdNET-Analyzer
pip3 install -r requirements.txt
mkdir -p checkpoints/V2.3
# Download model + label files manually or script it if source available
