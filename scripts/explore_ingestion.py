from nfl_ml.ingestion.sleeper import SleeperClient


LEAGUE_ID = "1251653519144914944"

client = SleeperClient()

users = client.get_users(LEAGUE_ID)
rosters = client.get_rosters(LEAGUE_ID)
matchups = client.get_matchups(LEAGUE_ID, 8)

print(type(users))
print(type(users[0]))

print(users[0]["display_name"])
print(users[0]["user_id"])

print(type(rosters))
print(type(rosters[0]))

print(rosters[0]["roster_id"])
print(rosters[0]["owner_id"])

first_user = users[0]

first_roster = None

first_matchup = None

for roster in rosters:
    if roster["owner_id"] == first_user["user_id"]:
        first_roster = roster

for matchup in matchups:
    if matchup["roster_id"] == first_roster["roster_id"]:
        first_matchup = matchup

print(first_user["display_name"])
print(first_user.get("metadata", {}).get("team_name"))
print(first_roster["roster_id"])
print(first_matchup["points"])
print(first_matchup["matchup_id"])


roster_by_owner = {
    roster["owner_id"]: roster
    for roster in rosters
}

matchup_by_roster = {
    matchup["roster_id"]: matchup
    for matchup in matchups
}

league_rows = []

for user in users:
    roster = roster_by_owner.get(user["user_id"])

    matchup = None
    if roster is not None:
        matchup = matchup_by_roster.get(roster["roster_id"])

    league_rows.append(
        {
            "manager": user["display_name"],
            "team_name": user.get("metadata", {}).get("team_name"),
            "roster_id": roster["roster_id"] if roster else None,
            "week_8_points": matchup["points"] if matchup else None,
            "matchup_id": matchup["matchup_id"] if matchup else None,
        }
    )

for row in league_rows:
    print(row)

matchups_by_id = {}

for row in league_rows:
    matchup_id = row["matchup_id"]

    if matchup_id not in matchups_by_id:
        matchups_by_id[matchup_id] = []

    matchups_by_id[matchup_id].append(row)

for matchup_id in sorted(matchups_by_id):
    teams = matchups_by_id[matchup_id]

    team_1 = teams[0]
    team_2 = teams[1]

    if team_1["week_8_points"] > team_2["week_8_points"]:
        winner = team_1
        loser = team_2

    elif team_2["week_8_points"] > team_1["week_8_points"]:
        winner = team_2
        loser = team_1
    else:
        print(
            team_1["team_name"],
            "tied",
            team_2["team_name"],
            team_1["week_8_points"],
            team_2["week_8_points"],
        )
        continue

    margin = round(
        winner["week_8_points"] - loser["week_8_points"],
        2,
    )

    print(winner["team_name"],"beat", loser["team_name"], winner["week_8_points"], "-", loser["week_8_points"], "by", margin, "points")


