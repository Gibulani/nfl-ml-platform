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