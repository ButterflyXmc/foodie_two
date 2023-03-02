from flask import request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app
import bcrypt
import uuid

# need to request email and pass from client table 
# then store client id and token in client session table
@app.post('/api/client-login')
def client_login():
    token = uuid.uuid4().hex
    email = request.json.get("email")
    password = request.json.get("password")
    salt = bcrypt.gensalt()
    hash_result = bcrypt.hashpw(password.encode(), salt)
    result = run_statement("CALL client_login(?,?,?)", [email, hash_result, token])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"


@app.delete('/api/client-login')
def logout():
    token = request.json.get("token")
    result = run_statement("CALL delete_client_login(?)", [token])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"