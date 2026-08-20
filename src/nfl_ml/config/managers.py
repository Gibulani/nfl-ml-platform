import json
from pathlib import Path

from nfl_ml.domain.models import Manager

def load_managers(config_path: Path) -> dict[str, Manager]:
    with config_path.open(encoding="utf-8") as file:
        config = json.load(file)

    managers_by_sleeper_id = {}

    for manager_data in config["managers"]:
        manager = Manager(
            manager_id=manager_data["manager_id"],
            name=manager_data["name"],
        )

        for sleeper_user_id in manager_data["sleeper_user_ids"]:
            managers_by_sleeper_id[sleeper_user_id] = manager

    return managers_by_sleeper_id