import json
from multiprocessing.context import assert_spawning

class TestAPICase():

    # base.html render
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == "200 OK"
        assert  b"<h2>Home</h2>" in res.data

######################   POKEMON

    # Displays data in home.html
    def test_get_pokemon_handler(self, api):
        res = api.get("/pokemon")
        assert res.status == "200 OK"
        assert b"<h4>squirtle</h4>" in res.data
        assert b"<h4>wartortle</h4>" in res.data
        assert b"<h4>blastoise</h4>" in res.data

    # SHOW test
    def test_show_pokemon_handler(self, api):
        res = api.get('/pokemon/2')
        assert res.status == "200 OK"
        assert res.json['name'] == "wartortle"

    # POST test and adds new data to home.html
    def test_post_pokemon_handler(self, api):
        obj = {"id": 4, "name": 'pokemon1', 'nickname': "poke",  "type": "Water", "level": "6"}
        res = api.post('/pokemon', data=obj)
        res2 = api.get("/pokemon")
        print(res2.data)
        assert res.status == '201 CREATED'
        assert  b"<h4>pokemon1</h4>" in res2.data

    # INDEX test - from tom
    def test_api_getall(self, api):
        res = api.get('/api/pokemon')
        assert res.status == '200 OK'
        assert len(res.json) == 3

    # SHOW test - test from tom
    def test_api_single(self, api):
        res = api.get('/api/pokemon/3')
        assert res.status == '200 OK'
        assert res.json['name']=="blastoise"

    # DELETE test - test from tom
    def test_api_single_delete(self, api):
        res = api.delete('/api/pokemon/1')
        assert res.status == '204 NO CONTENT'
    # POST test
    def test_api_single_post(self, api):
        mock_data = json.dumps({'name': 'pokemon'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/pokemon', data=mock_data, headers=mock_headers)
        assert res.status == '201 CREATED'
        assert res.json['id'] == 4
        assert res.json['name'] == "pokemon"


    ########################### Form

    def test_subscribe_handler(self, api):
        res = api.get("/subscribe")
        assert res.status == "200 OK"
        assert b"<h1>Subscribe To My Pokemon Newsletter</h1>" in res.data
        assert "Subscribe" in res.text

    def test_submit(self, api):
        obj = {"firstName": "Alex", "lastName": "Carlino-Rackett", "email": "alex@alex.com"}
        res = api.post("/submit", data=obj)
        
        assert res.status == "201 CREATED"
    



    ########################### Error tests

    # Not Found - 404
    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']

    # Bad Request - 400
    def test_bad_request(self, api):
        mock_pokemon = json.dumps({"firstName": "sam"})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/pokemon', data=mock_pokemon, headers=mock_headers)
        assert res.status == '400 BAD REQUEST'
        assert 'Oops!' in res.json['message']

    # Method Not ALLOWED - 405
    def test_method_not_allowed(self, api):
        obj = {"firstName": "Alex"}
        res = api.post('/subscribe', data=obj)
        res2 = api.get("/form")
        assert res.status == '405 METHOD NOT ALLOWED'
        assert 'Oops!' in res.json['message']
        # So the route has no POST method hence the error
    # Internal Error - 500
    # def test_internal_error(self, api):
    #     res = api.get('/pokemon/8')
    #     assert res.status == '500 INTERNAL ERROR'
    #     assert "It's not you, it's us" in res.json['message']
