from nfl_ml.ingestion.sleeper import DEFAULT_TIMEOUT_SECONDS, SleeperClient


class FakeResponse:
    def __init__(self, data):
        self.data = data
        self.raise_for_status_called = False

    def raise_for_status(self):
        self.raise_for_status_called = True

    def json(self):
        return self.data


class FakeSession:
    def __init__(self, response):
        self.response = response
        self.requested_url = None
        self.requested_timeout = None

    def get(self, url, timeout):
        self.requested_url = url
        self.requested_timeout = timeout
        return self.response


def test_get_league_returns_league_data():
    league_data = {
        "name": "Test League",
        "season": "2026",
        "total_rosters": 12,
    }

    response = FakeResponse(league_data)
    session = FakeSession(response)

    client = SleeperClient(
        base_url="https://example.com",
        session=session,
    )

    result = client.get_league("12345")

    assert result == league_data
    assert session.requested_url == "https://example.com/league/12345"
    assert session.requested_timeout == DEFAULT_TIMEOUT_SECONDS
    assert response.raise_for_status_called


def test_get_users_returns_user_data():
    user_data = [
        {
            "user_id": "user-1",
            "display_name": "Test Manager",
        }
    ]

    response = FakeResponse(user_data)
    session = FakeSession(response)

    client = SleeperClient(
        base_url="https://example.com",
        session=session,
    )

    result = client.get_users("12345")

    assert result == user_data
    assert session.requested_url == "https://example.com/league/12345/users"
    assert session.requested_timeout == DEFAULT_TIMEOUT_SECONDS
    assert response.raise_for_status_called

def test_get_matchups_returns_matchup_data():
    matchup_data = [
        {
            "roster_id": 1,
            "matchup_id": 4,
            "points": 91.22,
        }
    ]

    response = FakeResponse(matchup_data)
    session = FakeSession(response)

    client = SleeperClient(
        base_url="https://example.com",
        session=session,
    )

    result = client.get_matchups("12345", 8)

    assert result == matchup_data
    assert session.requested_url == "https://example.com/league/12345/matchups/8"
    assert session.requested_timeout == DEFAULT_TIMEOUT_SECONDS
    assert response.raise_for_status_called

def test_get_rosters_returns_roster_data():
    roster_data = [
        {
            "league_id": "12345",
            "owner_id": "user-1",
            "roster_id": 1,
        }
    ]

    response = FakeResponse(roster_data)
    session = FakeSession(response)

    client = SleeperClient(
        base_url="https://example.com",
        session=session,
    )

    result = client.get_rosters("12345")

    assert result == roster_data
    assert session.requested_url == "https://example.com/league/12345/rosters"
    assert session.requested_timeout == DEFAULT_TIMEOUT_SECONDS
    assert response.raise_for_status_called

