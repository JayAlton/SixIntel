from flask import Flask, render_template
import json
import os
from scraper.liquipedia_scraper import get_r6_standings

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route('/<region>')
def region_combined(region):
    region = region.upper()
    if region not in ['NA', 'EU']:
        return "Region not found", 404

    try:
        with open(f"data/{region.lower()}_stats.json") as f:
            stats = json.load(f)
        with open(f"data/{region.lower()}_standings.json") as f:
            standings = json.load(f)
    except FileNotFoundError:
        return "Data not found", 404

    return render_template("combined.html", region=region, stats=stats, standings=standings)

if __name__ == "__main__":
    app.run(debug=True)
