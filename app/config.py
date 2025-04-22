import os
import json

CONFIG_PATH = os.path.expanduser("~/birdnet-pi/data/config.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("Config not found. Run setup_latlon.py first.")
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def get_lat_lon():
    config = load_config()
    return config.get("lat"), config.get("lon")

def get_config_value(key, default=None):
    config = load_config()
    return config.get(key, default)
