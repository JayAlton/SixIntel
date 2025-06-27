from flask import Flask, render_template
from scraper.liquipedia_scraper import get_r6_standings

app = Flask(__name__)

# Scrape once at startup
standings_cache = get_r6_standings()

@app.route("/")
def index():
    return render_template("index.html", standings=standings_cache)

if __name__ == "__main__":
    app.run(debug=True)
