from nfl_ml.ingestion.sleeper import SleeperClient
from nfl_ml.domain.models import Manager
from nfl_ml.transformations.sleeper_to_domain import (
    to_league_season,
    to_manager_season,
)

LEAGUE_ID = "1251653519144914944"

client = SleeperClient()

league_data = client.get_league(LEAGUE_ID)
users = client.get_users(LEAGUE_ID)
rosters = client.get_rosters(LEAGUE_ID)

league_season = to_league_season(league_data)

print(league_season)

mike = Manager(
    manager_id=1,
    name="Mike",
)

mike_user = next(
    user
    for user in users
    if user["display_name"] == "Gibulani"
)

mike_roster = next(
    roster
    for roster in rosters
    if roster["owner_id"] == mike_user["user_id"]
)

mike_2025 = to_manager_season(
    manager=mike,
    league_season=league_season,
    user_data=mike_user,
    roster_data=mike_roster,
)

print(mike_2025)


for user in users:
    print(
        user["user_id"],
        user["display_name"],
        user.get("metadata", {}).get("team_name"),
    )