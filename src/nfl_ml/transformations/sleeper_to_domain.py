from typing import Any

from nfl_ml.domain.models import LeagueSeason, Manager, ManagerSeason


def to_league_season(league_data: dict[str, Any]) -> LeagueSeason:
    return LeagueSeason(
        season=int(league_data["season"]),
        league_name=league_data["name"],
        sleeper_league_id=league_data["league_id"],
        number_of_teams=league_data["settings"]["num_teams"],
        number_of_playoff_teams=league_data["settings"]["playoff_teams"],
        previous_sleeper_league_id=league_data["previous_league_id"],
    )

def to_manager_season(
    manager: Manager,
    league_season: LeagueSeason,
    user_data: dict[str, Any],
    roster_data: dict[str, Any],
) -> ManagerSeason:   

    points_for = (
        roster_data["settings"]["fpts"] 
        + roster_data["settings"]["fpts_decimal"] / 100
    )

    points_against = (
        roster_data["settings"]["fpts_against"] 
        + roster_data["settings"]["fpts_against_decimal"] / 100
    )

    return ManagerSeason(
        manager=manager,
        league_season=league_season,
        sleeper_user_id=user_data["user_id"],
        sleeper_display_name=user_data["display_name"],
        team_name=user_data.get("metadata", {}).get("team_name"),
        roster_id=roster_data["roster_id"],
        wins=roster_data["settings"]["wins"],
        losses=roster_data["settings"]["losses"],
        points_for=points_for,
        points_against=points_against,
    )
    
  