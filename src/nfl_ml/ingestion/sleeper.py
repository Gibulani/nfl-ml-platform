from typing import Any

import requests


BASE_URL = "https://api.sleeper.app/v1"
DEFAULT_TIMEOUT_SECONDS = 10


class SleeperClient:
    def __init__(self, base_url: str = BASE_URL, session: requests.Session | None = None,):
        self.base_url = base_url
        self.session = session or requests.Session()

    def get_league(self, league_id: str) -> dict[str, Any]:
        url = f"{self.base_url}/league/{league_id}"

        response = self.session.get(
            url,
            timeout=DEFAULT_TIMEOUT_SECONDS,
        )

        response.raise_for_status()

        return response.json()