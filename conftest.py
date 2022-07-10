import pytest
import server
from controllers import pokemon

@pytest.fixture
def api(monkeypatch):
    test_pokemon = [
        {'id': 1, 'name': 'squirtle'},
        {'id': 2, 'name': 'wartortle'},
        {'id': 2, 'name': 'blastoise'},
    ]
    monkeypatch.setattr(pokemon, "pokemonlist", test_pokemon)
    api = server.server.test_client()
    return api


