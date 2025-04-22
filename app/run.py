import time
import logging
from config import load_config
from recorder import record_audio
from detector import analyze_audio
from storage import save_detections, init_db

AUDIO_DIR = os.path.expanduser("~/birdnet-pi/audio")

logging.basicConfig(
    filename=os.path.expanduser("~/birdnet-pi/logs/app.log"),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def main():
    config = load_config()
    init_db()
    logging.info("Starting BirdNET Pi loop")

    while True:
        path = record_audio(AUDIO_DIR, config.get("min_free_space_mb", 500))
        if path:
            timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            results = analyze_audio(path)
            if results:
                save_detections(timestamp, path, results)
        time.sleep(5)

if __name__ == "__main__":
    main()
