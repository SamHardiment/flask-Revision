from werkzeug.exceptions import BadRequest

pokemonlist = [
    {'id': 1, 'name': 'Squritle', "nickname": 'Squritle', "type": "Water", "level": 12},
    {'id': 2, 'name': 'Wartortle', 'nickname': 'Wartortle', "type": "Water",  "level": 28},
    {'id': 3, 'name': 'Blastoise', 'nickname': 'Blastoise', "type": "Water",  "level": 44},
]

def index(req):
    return [p for p in pokemonlist], 200

def create(req):
    new_pokemon = req.get_json()
    new_pokemon['id'] = (sorted([m['id'] for m in pokemonlist])[-1] + 1)
    pokemonlist.append(new_pokemon)
    return pokemonlist, 201

def show(req, uid):
    return find_by_uid(uid), 200

def find_by_uid(uid):
    try:
        return next(p for p in pokemonlist if p['id'] == uid)
    except:
        raise BadRequest(f"We don't hae a pokemon with id {uid}")

def update(req, uid):
    p_to_update = find_by_uid(uid)
    request = req.get_json()
    for key, val in request.items():
        p_to_update[key] = val
    return p_to_update, 202

def destroy(req, uid):
    p_to_delete = find_by_uid(uid)
    pokemonlist.remove(p_to_delete)
    return p_to_delete, 204
