from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_r6_standings():
    url = "https://liquipedia.net/rainbowsix/North_America_League/2025/Stage_1"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service, options=options)

    print("Loading page in browser...")
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    container = soup.find("div", class_="table-responsive toggle-area toggle-area-6")
    if not container:
        print("⚠️ Could not find standings container div.")
        return []

    table = container.find("table")
    if not table:
        print("⚠️ Could not find table inside standings container.")
        return []
    
    standings = []
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) < 6:
            continue
        team_tag = cols[1].find("a")
        team = team_tag.get_text(strip=True) if team_tag else cols[1].get_text(strip=True)
        wins = cols[2].get_text(strip=True)
        losses = cols[3].get_text(strip=True)
        points = cols[5].get_text(strip=True)
        standings.append({
            "team": team,
            "wins": wins,
            "losses": losses,
            "points": points
        })

    print(f"Scraped {len(standings)} teams from live page.")
    return standings
