import json

from nfl_ml.config.managers import load_managers


def test_load_managers_maps_sleeper_ids_to_managers(tmp_path):

    config = {
        "managers": [
            {
                "manager_id": 1,
                "name": "Test Manager",
                "sleeper_user_ids": [
                    "old-user-id",
                    "new-user-id",
                ],
            }
        ]
    }

    config_path = tmp_path / "managers.json"

    with config_path.open("w", encoding="utf-8") as file:
        json.dump(config, file)

    managers = load_managers(config_path)

   
    assert managers["old-user-id"].manager_id == 1
    assert managers["new-user-id"].manager_id == 1
    assert managers["old-user-id"].name == "Test Manager"
    assert managers["new-user-id"].name == "Test Manager"
    assert managers["old-user-id"] is managers["new-user-id"]