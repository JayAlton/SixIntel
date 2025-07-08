from flask import Flask, render_template
import json
import os
from scraper.liquipedia_scraper import get_r6_standings

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/<region>")
def region_stats(region):
    with open(f"data/{region}_standings.json") as f:
        standings = json.load(f)

    # Sort by points (int), then rd (int), both descending
    standings.sort(key=lambda t: (int(t["points"]), int(t["rd"])), reverse=True)

    return render_template("standings.html", region=region.upper(), standings=standings)


@app.route('/<region>/standings')
def region_standings(region):
    standings = get_r6_standings(region)
    return render_template('standings.html', region=region.upper(), standings=standings)

@app.route('/<region>/stats')
def region_stats(region):
    try:
        file_path = os.path.join("data", f"{region.lower()}_stats.json")
        with open(file_path, "r") as f:
            stats = json.load(f)
    except FileNotFoundError:
        return f"No stats found for region: {region.upper()}", 404

    return render_template("stats.html", stats=stats, region=region.upper())

if __name__ == "__main__":
    app.run(debug=True)
