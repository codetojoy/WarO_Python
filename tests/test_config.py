
from config import build_config_from_json

def test_build_config_from_json():
    json_str = """
{
"num_cards": 20,
"num_games": 1,
"is_verbose": true,
"players": [
    {"name": "beethoven", "strategy": "next_card"},
    {"name": "chopin", "strategy": "next_card"},
    {"name": "mozart", "strategy": "next_card"}
]
}
"""
    # test
    config = build_config_from_json(json_str)

    assert config.num_cards == 20
    assert config.num_games == 1
    assert config.is_verbose
    assert len(config.players) == 3
