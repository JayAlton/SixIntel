import json

# Load files
with open("data/na_stats.json", "r") as f:
    players = json.load(f)

with open("data/na_standings.json", "r") as f:
    teams = json.load(f)

def get_player_obj(name):
    for p in players:
        if p["player"].lower() == name.lower():
            return p
    return None

def get_team_obj(name):
    for t in teams:
        if t["team"].lower() == name.lower():
            return t
    return None

def update_team(team, scored, conceded):
    wins, ot_wins, ot_losses, losses = map(int, team["record"].split("-"))
    if scored > conceded:
        wins += 1
    else:
        losses += 1
    team["record"] = f"{wins}-{ot_wins}-{ot_losses}-{losses}"

    sr, sc = map(int, team["rnd"].split("-"))
    sr += scored
    sc += conceded
    team["rnd"] = f"{sr}-{sc}"
    team["rd"] = str(sr - sc)

def main():
    print("== Match Setup ==")
    team1_name = input("Team 1 name: ").strip()
    team2_name = input("Team 2 name: ").strip()
    team1_score = int(input(f"{team1_name} rounds won: "))
    team2_score = int(input(f"{team2_name} rounds won: "))

    team1 = get_team_obj(team1_name)
    team2 = get_team_obj(team2_name)

    if not team1 or not team2:
        print("One or both teams not found in team data.")
        return

    update_team(team1, team1_score, team2_score)
    update_team(team2, team2_score, team1_score)

    print("\n== Player Stats Input ==")
    for _ in range(10):
        player_name = input("Player name (or 'done' to finish): ").strip()
        if player_name.lower() == "done":
            break

        player = get_player_obj(player_name)
        if not player:
            print(f"Player {player_name} not found.")
            continue

        new_kills = int(input(f"  Kills for {player_name}: "))
        new_deaths = int(input(f"  Deaths for {player_name}: "))
        kills = player["kills"] + new_kills
        deaths = player["deaths"]  + new_deaths
        maps_played = player["maps"] + 1

        kd_diff = kills - deaths
        player["kills"] = kills
        player["deaths"] = deaths    
        player["k_d"] = f"{kills}-{deaths} ({'+' if kd_diff >= 0 else ''}{kd_diff})"
        player["rating"] = f"{kills / max(deaths, 1):.2f}"
        player["maps"] = maps_played

        print(f"  Updated {player_name}'s kills, deaths, k/d, and maps played.")

    # Save back the data
    with open("data/na_stats.json", "w") as f:
        json.dump(players, f, indent=2)

    with open("data/na_standings.json", "w") as f:
        json.dump(teams, f, indent=2)

    print("\n✅ Match data updated successfully.")

if __name__ == "__main__":
    main()
