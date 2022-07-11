import pytest
import server
from controllers import pokemon, subscribers

@pytest.fixture
def api(monkeypatch):
    test_pokemon = [
        {'id': 1, 'name': 'squirtle'},
        {'id': 2, 'name': 'wartortle'},
        {'id': 3, 'name': 'blastoise'},
    ]
    monkeypatch.setattr(pokemon, "pokemonlist", test_pokemon)
    test_subscribers = [
        {"id": 2, "firstName": "Sam", "lastName": "Hardiment", "email": "sam@sam.com"},
    ]
    monkeypatch.setattr(subscribers, "subscribers", test_subscribers)
    api = server.server.test_client()
    return api

