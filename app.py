from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Load data
df = pd.read_csv("campaign_data.csv")

@app.route("/")
def home():
    return "Marketing Campaign API is Live!"

@app.route("/api/campaigns", methods=["GET"])
def get_campaigns():
    platform = request.args.get("platform")
    if platform:
        data = df[df["Platform"].str.lower() == platform.lower()]
    else:
        data = df
    return jsonify(data.to_dict(orient="records"))

@app.route("/api/refresh", methods=["POST"])
def refresh_data():
    global df
    df = pd.read_csv("campaign_data.csv")
    return jsonify({"status": "refreshed"})

# Run on specified port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
