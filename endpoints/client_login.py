from flask import request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app
import bcrypt
import uuid

@app.post('/api/client-login')
def client_login():
    token = uuid.uuid4().hex
    # token = request.json.get("token")
    email = request.json.get("email")
    password = request.json.get("password")
    salt = bcrypt.gensalt()
    hash_result = bcrypt.hashpw(password.encode(), salt)
    result = run_statement("CALL client_login(?,?,?)", [email, hash_result, token])
    if(type(result)== list):
        if result == []:
            return make_response(jsonify("Incorrect input, try again!"),500)
        elif email == None:
            return "Enter an email"
        elif password == None:
            return "Enter a password"
        else:
            return make_response(jsonify(result), 500)
        


@app.delete('/api/client-login')
def logout():
    token = request.json.get("token")
    result = run_statement("CALL delete_client_login(?)", [token])
    if result == None:
        return make_response(jsonify("Logged Out!"),200)
    else:
        return make_response(jsonify(result), 500)