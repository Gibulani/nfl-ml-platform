from typing import Any

from nfl_ml.domain.models import LeagueSeason


def to_legacy_league_season(legacy_data: dict[str, Any]) -> LeagueSeason:
    return LeagueSeason(
            season=int(legacy_data["season"]),
            league_name=legacy_data["league_name"],
            sleeper_league_id=None,
            number_of_teams=legacy_data["number_of_teams"],
            number_of_playoff_teams=legacy_data["number_of_playoff_teams"],
            previous_sleeper_league_id=None,
)