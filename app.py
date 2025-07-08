from flask import Flask, render_template
import json
import os
from scraper.liquipedia_scraper import get_r6_standings

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route('/<region>/overview')
def region_overview(region):
    if region not in ['NA', 'EU']:
        return "Region not found", 404

    # Load standings (from scraper or file)
    try:
        standings = get_r6_standings(region)
    except Exception:
        standings = []

    # Load stats from JSON file
    try:
        file_path = os.path.join("data", f"{region.lower()}_stats.json")
        with open(file_path, "r") as f:
            stats = json.load(f)
    except FileNotFoundError:
        stats = []

    return render_template('combined.html', region=region.upper(), standings=standings, stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
