from dataclasses import dataclass

@dataclass(frozen=True)
class Manager:
    manager_id: int
    name: str

@dataclass(frozen=True)
class LeagueSeason:
    season: int
    league_name: str
    sleeper_league_id: str | None
    number_of_teams: int
    number_of_playoff_teams: int | None
    previous_sleeper_league_id: str | None


@dataclass(frozen=True)
class ManagerSeason:
    manager: Manager
    league_season: LeagueSeason
    sleeper_user_id: str | None
    sleeper_display_name: str | None
    team_name: str | None
    roster_id: int | None
    wins: int
    losses: int
    points_for: float | None
    points_against: float | None
    final_position: int | None = None
 