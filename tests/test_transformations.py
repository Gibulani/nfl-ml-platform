from nfl_ml.domain.models import LeagueSeason, Manager

from nfl_ml.transformations.sleeper_to_domain import (
    to_league_season,
    to_manager_season,
)


def test_to_league_season_transforms_sleeper_data():
    league_data = {
        "name": "Tyneside Superb Owl",
        "season": "2025",
        "league_id": "2",
        "previous_league_id": "1",
        "settings": {
            "num_teams": 12,
            "playoff_teams": 6,
        },
    }

    league_season = to_league_season(league_data)

    assert league_season.season == 2025
    assert league_season.league_name == "Tyneside Superb Owl"
    assert league_season.sleeper_league_id == "2"
    assert league_season.number_of_teams == 12
    assert league_season.number_of_playoff_teams == 6
    assert league_season.previous_sleeper_league_id == "1"


def test_to_manager_season_transforms_sleeper_data():
    league_data = {
        "name": "Tyneside Superb Owl",
        "season": "2025",
        "league_id": "2",
        "previous_league_id": "1",
        "settings": {
            "num_teams": 12,
            "playoff_teams": 6,
        },
    }

    manager = Manager(
        manager_id=1,
        name="Mike",
    ) 

    user_data = {
        "user_id": "1",
        "display_name": "Gibulani",
        "metadata": {
            "team_name": "F the QB"                
        },
    }

    roster_data = {
        "roster_id": 1,
        "settings": {
            "wins": 6,
            "losses": 2,
            "fpts": 800,
            "fpts_decimal": 25,
            "fpts_against": 650,
            "fpts_against_decimal": 75,
        },
    }

    league_season = to_league_season(league_data)
    manager_season = to_manager_season(manager, league_season, user_data, roster_data)

    assert manager_season.manager == manager
    assert manager_season.league_season == league_season
    assert manager_season.sleeper_user_id == "1"
    assert manager_season.sleeper_display_name == "Gibulani"
    assert manager_season.team_name == "F the QB"
    assert manager_season.roster_id == 1
    assert manager_season.wins == 6
    assert manager_season.losses == 2
    assert manager_season.points_for == 800.25
    assert manager_season.points_against == 650.75

