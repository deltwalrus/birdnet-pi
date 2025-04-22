import subprocess
import os
import tempfile
import csv
import logging
from config import get_lat_lon

BIRDNET_PATH = os.path.expanduser("~/BirdNET-Analyzer")
MODEL_PATH = os.path.join(BIRDNET_PATH, "checkpoints", "V2.3/BirdNET_GLOBAL_6K_V2.3_Model_FP16.tflite")
LABELS_PATH = os.path.join(BIRDNET_PATH, "checkpoints", "V2.3/labels.txt")

def analyze_audio(filepath):
    lat, lon = get_lat_lon()
    tmp_out = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
    cmd = [
        "python3", os.path.join(BIRDNET_PATH, "analyze.py"),
        "--i", filepath,
        "--o", os.path.dirname(tmp_out.name),
        "--lat", str(lat),
        "--lon", str(lon),
        "--model", MODEL_PATH,
        "--labels", LABELS_PATH,
        "--min_conf", "0.6"
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        result_path = tmp_out.name.replace(".csv", ".BirdNET.results.csv")
        if os.path.exists(result_path):
            with open(result_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader)
        else:
            logging.warning(f"Result CSV not found: {result_path}")
    except Exception as e:
        logging.error(f"BirdNET analysis failed: {e}")
    finally:
        tmp_out.close()

    return []
