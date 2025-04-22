import os
import datetime
import subprocess
import shutil
import logging

def has_enough_space(min_mb):
    total, used, free = shutil.disk_usage("/")
    return free // (1024 * 1024) > min_mb

def record_audio(audio_dir, min_mb):
    if not has_enough_space(min_mb):
        logging.warning("Low disk space. Skipping recording.")
        return None

    now = datetime.datetime.now()
    date_path = now.strftime("%Y-%m-%d")
    filename = now.strftime("%H-%M-%S.wav")
    full_dir = os.path.join(audio_dir, date_path)
    os.makedirs(full_dir, exist_ok=True)
    filepath = os.path.join(full_dir, filename)

    try:
        subprocess.run(["arecord", "-D", "plughw:1", "-f", "cd", "-t", "wav", "-d", "60", "-r", "44100", filepath], check=True, timeout=70)
        return filepath
    except subprocess.TimeoutExpired:
        logging.error("Recording timed out.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Recording failed: {e}")
    return None
