from flask import Flask, render_template, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.expanduser("~/birdnet-pi/data/detections.db")

@app.route("/")
def index():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT timestamp, species, confidence FROM detections ORDER BY timestamp DESC LIMIT 100")
        data = cur.fetchall()
    return render_template("index.html", detections=data)

@app.route("/status")
def status():
    import shutil, time, os
    total, used, free = shutil.disk_usage("/")
    temp_path = '/sys/class/thermal/thermal_zone0/temp'
    cpu_temp = round(int(open(temp_path).read()) / 1000, 1) if os.path.exists(temp_path) else None
    uptime = time.time() - os.stat('/proc/1').st_ctime
    return jsonify({
        "disk_free_gb": round(free / (1024**3), 1),
        "disk_used_percent": round(used / total * 100, 1),
        "cpu_temp_c": cpu_temp,
        "uptime": round(uptime / 3600, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
