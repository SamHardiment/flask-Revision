import json
from multiprocessing.context import assert_spawning

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == "200 OK"

    def test_get_pokemon_handler(self, api):
        res = api.get("/pokemon")
        # print(dir(res))
        print(res)
        assert res.status == "200 OK"
        assert len(res.json) == 3

    def test_show_pokemon_handler(self, api):
        res = api.get('/pokemon/2')
        assert res.status == "200 OK"
        assert res.json['name'] == "wartortle"

    # def test_post_pokemon_handler(self, api):
    #     mock_pokemon = json.dumps({'name': 'pokemon1', "nickname": "sam", "type": "water", "level": 2})
    #     mock_headers = {'Content-Type': 'application/json'}

    #     res = api.post('/pokemon', data=mock_pokemon, headers=mock_headers)
    #     assert res.status == '201 CREATED'
    #     assert res.json['pokemon']['id'] == 4

    # test from tom
    def test_api_getall(self, api):
        res = api.get('/api/pokemon')
        assert res.status == '200 OK'
        assert len(res.json) == 3

    # test from tom
    def test_api_single(self, api):
        res = api.get('/api/pokemon/3')
        assert res.status == '200 OK'
        assert res.json['name']=="blastoise"

    # test from tom
    def test_api_single_delete(self, api):
        res = api.delete('/api/pokemon/1')
        assert res.status == '204 NO CONTENT'

    # Error tests
    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']

    def test_bad_request(self, api):
        mock_pokemon = json.dumps({"firstName": "sam"})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/pokemon', data=mock_pokemon, headers=mock_headers)
        assert res.status == '400 BAD REQUEST'
        assert 'Oops!' in res.json['message']

    def test_internal_error(self, api):
        res = api.get('/pokemon')
        assert res.status == '500 INTERNAL ERROR'
        assert "It's not you, it's us" in res.json['message']
