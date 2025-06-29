from bs4 import BeautifulSoup
import json
import os
import time

def get_r6_standings(region):
    print("Loading standings from local JSON file...")
    path = f"data/{region.lower()}_standings.json"
    with open(path) as f:
        data = json.load(f)
    return data
