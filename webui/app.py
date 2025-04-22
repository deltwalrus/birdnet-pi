from flask import Flask, render_template, jsonify
import sqlite3, shutil, time, os

app = Flask(__name__)
DB_PATH = os.path.expanduser("~/birdnet-pi/data/detections.db")

@app.route("/")
def index():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT timestamp, species, confidence FROM detections ORDER BY timestamp DESC LIMIT 100")
        rows = cur.fetchall()
    return render_template("index.html", detections=rows)

@app.route("/status")
def status():
    total, used, free = shutil.disk_usage("/")
    temp_c = None
    try:
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            temp_c = round(int(f.read().strip()) / 1000, 1)
    except: pass
    uptime = round(time.time() - os.stat('/proc/1').st_ctime, 1)
    return jsonify({
        "disk_free_gb": round(free / (1024**3), 1),
        "disk_used_percent": round(used / total * 100, 1),
        "cpu_temp_c": temp_c,
        "uptime_hours": round(uptime / 3600, 1)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
