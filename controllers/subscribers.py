subscribers = [
    {'id': 1, 'firstName': 'Sam', "lastName": 'Hardiment', "email": "sam@sam.com"},
]
def create(req):
    new_sub = req.get_json()
    new_sub['id'] = (sorted([s['id'] for s in subscribers])[-1] + 1) #couldnt be assed looking at this, too late at night :S 
    subscribers.append(new_sub)
    # return pokemonlist, 201 #changed because i think u need to return the new word
    return subscribers, 201
