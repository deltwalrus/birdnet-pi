import os
import json

CONFIG_PATH = os.path.expanduser("~/birdnet-pi/data/config.json")

def run_setup():
    print("Initial BirdNET Setup")
    lat = input("Enter your latitude (e.g. 40.7128): ").strip()
    lon = input("Enter your longitude (e.g. -74.0060): ").strip()

    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)

    config = {
        "lat": float(lat),
        "lon": float(lon),
        "log_level": "INFO",
        "min_free_space_mb": 500
    }

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    print("Setup complete. Config saved to:", CONFIG_PATH)

if __name__ == "__main__":
    run_setup()
