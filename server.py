from flask import Flask, request, render_template, url_for
from flask_cors import CORS
from flask import jsonify
from werkzeug import exceptions

import smtplib
from flask_mailman import Mail, EmailMessage
# This is for creatingg a email link that will expire
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


from controllers import pokemon, subscribers



# // Creates an instance of the flask object
# __name__ represents the name of the application package and it's used by Flask to identify resources like templates static assests and the instance folder
server = Flask(__name__)
CORS(server)
mail = Mail(server)

@server.route('/')
def home():
    return render_template('base.html'), 200


@server.route('/pokemon', methods=['GET', 'POST'])
def pokemonList_handler():
    fns = {
        'GET': pokemon.index,
        # 'POST': pokemon.create
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
@server.route('/api/pokemon', methods=['GET',"POST"])
def pokemon_all():
    fns = {
        'GET' : pokemon.index,
        'POST' : pokemon.create
    }
    resp, code = fns[request.method](request)  
    return jsonify(resp), code 

@server.route('/api/pokemon/<int:poke_id>', methods=['GET','DELETE',])
def pokemon_single(poke_id):
    fns = {
        'GET' : pokemon.show,
        'DELETE' : pokemon.destroy,
        
    }
    resp, code = fns[request.method](request,poke_id)  
    return jsonify(resp),code



#////////////////////////////////////////
#//////  Mailman

############################# Form email

@server.route('/subscribe')
def subscribe_handler():
    title = "Subscribe to my email newsletter"
    return render_template("form/subscribe.html", title=title)

@server.route('/submit', methods=["POST"])
def submit():
    # title = "Thank You!"
    # message = "You have been subcribed to my pokemon newsletter"
    # server = smtplib.SMTP("smtp.gmail,com", 587)
    # server.starttls()
    # server.login("sender_address", "sender_password")
    # server.sendmail("sender_address", request.form["emailInput"], message)

    fns = {
        'POST' : subscribers.create,
    }
    obj = { "firstName": request.form['firstNameInput'], 'lastName': request.form['lastNameInput'],  "email": request.form["emailInput"]}

    resp, code = fns[request.method](jsonify(obj))
    # return render_template("form/form.html", title=title, firstName = firstName, lastName = lastName, email = email)
    return render_template("form/form.html", title =title, sub = resp)

####################### Confirmation email stuff

# s = URLSafeTimedSerializer('secretKey')

# @server.route('/mailman', methods=['GET', 'POST'])
# def mailman_handler():
#     if request.method == 'GET':
#         return '<form action="/mailman" method="POST"><input name="email"><input type="submit"></form>'
#     # create a token for the link of the confirmation email
#     email = request.form['email']
#     # The salt is a way to sepeearate tokens that use the same input value
#     token = s.dumps(email, salt="email-confirm")
#     link = url_for('confirm_email', token=token, external=True)
#     msg = EmailMessage('Confirm Email', f"Your link is {link}", "samuelghardiment@gmail", [request.form['email']])
#     mail.send(msg)
#     return '<h1>The email you entered is {}. The token is {}</h1>'.format(email, token)


# make a route to get the email back. So we use the serializer to get the object back
# We use loads instead of dumps and we pass in the token and the same salt we used.
# max_age of 20 will give 20s untill the token expires

# @server.route('/confirm_email/<token>')
# def confirm_email(token):
#     try:
#         email = s.loads(token, salt="email-confirm", max_age=20)
#     except SignatureExpired:
#         return '<h2>The token is expired!</h2>'
#     except:
#         return '<h2>The token is invalid!</h2>'
#     return "<h2>The token works!</h2>"




# When the interprtr runs a module, the __name__ variable will be set as __main__ if the module that is being run is the main program
if __name__ == "__main__":
    server.run(debug=True)
