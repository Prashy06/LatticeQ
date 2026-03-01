from flask import Flask, render_template, jsonify, request
import ndr_engine

app = Flask(__name__)

MODE = "normal"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/set_mode", methods=["POST"])
def set_mode():
    global MODE
    data = request.json
    MODE = data.get("mode", "normal")
    return jsonify({"status": "ok"})

@app.route("/metrics")
def metrics():
    data = ndr_engine.get_dashboard_metrics(MODE)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)