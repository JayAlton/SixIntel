from flask import Flask, render_template
from scraper.liquipedia_scraper import get_r6_standings

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route('/<region>')
def region_home(region):
    if region not in ['na', 'eu']:
        return "Region not found", 404
    return render_template('region_home.html', region=region.upper())

@app.route('/<region>/standings')
def region_standings(region):
    standings = get_r6_standings(region)
    return render_template('standings.html', region=region.upper(), standings=standings)

@app.route('/<region>/stats')
def region_stats(region):
    return render_template('stats.html', region=region.upper(), stats=[])

if __name__ == "__main__":
    app.run(debug=True)
