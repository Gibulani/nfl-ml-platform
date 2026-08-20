from nfl_ml.ingestion.sleeper import SleeperClient


CURRENT_LEAGUE_ID = "1251653519144914944"

client = SleeperClient()

league_id = CURRENT_LEAGUE_ID
historical_users = {}

while league_id is not None:
    league = client.get_league(league_id)
    users = client.get_users(league_id)

    print(
        league["season"],
        league["league_id"],
        league["name"],
    )

    for user in users:
        historical_users[user["user_id"]] = user["display_name"]
        print(
            " ",
            league["season"],
            user["user_id"],
            user["display_name"],
            user.get("metadata", {}).get("team_name"),
        )

    league_id = league["previous_league_id"]

print()
print("Unique Sleeper users:")

for user_id, display_name in historical_users.items():
    print(user_id, display_name)

print()
print("Total:", len(historical_users))