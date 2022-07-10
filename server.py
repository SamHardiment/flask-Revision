from flask import Flask, request, render_template
from flask_cors import CORS
from flask import jsonify
from werkzeug import exceptions


from controllers import pokemon



# // Creates an instance of the flask object
# __name__ represents the name of the application package and it's used by Flask to identify resources like templates static assests and the instance folder
server = Flask(__name__)
CORS(server)


@server.route('/')
def home():
    return render_template('base.html'), 200


@server.route('/pokemon', methods=['GET', 'POST'])
def pokemonList_handler():
    fns = {
        'GET': pokemon.index,
        'POST': pokemon.create
    }
    if request.method == 'POST':
        obj = { "name": request.form['name'], 'nickname': request.form['nickname'],  "type": request.form["type"], "level": request.form["level"]}
        resp, code = fns[request.method](jsonify(obj))
    elif request.method == 'GET':
        resp, code = fns[request.method](request)
    return render_template('pokemon/home.html',  pokemon = resp), code

# @server.route('/pokemon', methods=['GET'])
# def pokemonList_get():
#     fns = {
#         'GET': pokemon.index,
#     }
#     resp, code = fns[request.method](request)
#     return render_template('pokemon/home.html', pokemon = resp), code

# @server.route('/pokemon', methods=['POST'])
# def pokemonList_POST():
#     fns = {
#         'POST': pokemon.create,
#     }
#     obj = { "name": request.form['name'], 'nickname': request.form['nickname'],  "type": request.form["type"], "level": request.form["level"]}
#     resp, code = fns[request.method](jsonify(obj))
#     return render_template('pokemon/home.html', pokemon = resp), code


@server.route('/pokemon/<int:pokemon_id>', methods=['GET', 'PATCH', 'DELETE'])
def pokemon_handler(pokemon_id):
    fns = {
        'GET': pokemon.show,
        'PATCH': pokemon.update,
        'DELETE': pokemon.destroy,
    }
    resp, code = fns[request.method](request, uid=pokemon_id)
    return jsonify(resp)


# //////////////////////////////////////////
#///tom added
@server.route('/api/pokemon', methods=['GET'])
def pokemon_all():
    fns = {
        'GET' : pokemon.index,
    }
    resp, code = fns[request.method](request)  
    return jsonify(resp)

@server.route('/api/pokemon/<int:poke_id>', methods=['GET','DELETE'])
def pokemon_single(poke_id):
    fns = {
        'GET' : pokemon.show,
        'DELETE' : pokemon.destroy
    }
    resp, code = fns[request.method](request,poke_id)  
    return jsonify(resp),code



# When the interprtr runs a module, the __name__ variable will be set as __main__ if the module that is being run is the main program

if __name__ == "__main__":
    server.run(debug=True)
