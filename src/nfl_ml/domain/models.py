from dataclasses import dataclass

@dataclass(frozen=True)
class Manager:
    manager_id: int
    name: str

@dataclass(frozen=True)
class LeagueSeason:
    season: int
    league_name: str
    sleeper_league_id: str
    number_of_teams: int
    number_of_playoff_teams: int
    previous_sleeper_league_id: str | None


@dataclass(frozen=True)
class ManagerSeason:
    manager: Manager
    league_season: LeagueSeason
    sleeper_user_id: str
    sleeper_display_name: str
    team_name: str | None
    roster_id: int
    wins: int
    losses: int
    points_for: float
    points_against: float
 