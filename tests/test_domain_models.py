from nfl_ml.domain.models import Manager, LeagueSeason, ManagerSeason


def test_manager_class():
    manager = Manager(
        manager_id=1,
        name="Mike",
    )   

    assert manager.manager_id == 1
    assert manager.name == "Mike"

def test_league_season_class():
    league_season = LeagueSeason(
        season=2025,
        league_name="TSO",
        sleeper_league_id="2",
        number_of_teams=12,
        number_of_playoff_teams=6,
        previous_sleeper_league_id="1",        
    )   

    assert league_season.season == 2025
    assert league_season.league_name == "TSO"

def test_manager_season_class():
    manager = Manager(
            manager_id=1,
            name="Mike",
    )   

    league_season = LeagueSeason(
        season=2025,
        league_name="TSO",
        sleeper_league_id="2",
        number_of_teams=12,
        number_of_playoff_teams=6,
        previous_sleeper_league_id="1",        
    )   

    manager_season = ManagerSeason(
        manager=manager,
        league_season=league_season,
        sleeper_user_id="1",
        sleeper_display_name="Gibulani",
        team_name="F The QB",
        roster_id=1,
        wins=6,
        losses=2,
        points_for=800,
        points_against=650,           
    )   

    assert manager_season.manager.name == "Mike"
    assert manager_season.sleeper_display_name == "Gibulani"
    assert manager_season.wins == 6

