from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app
import bcrypt
import uuid
#*Importing app from app as only a single app object is allowed
    
@app.post('/api/restaurant-login')
def resto_login():
    token = uuid.uuid4().hex
    email = request.json.get("email")
    password = request.json.get("password")
    salt = bcrypt.gensalt()
    hash_result = bcrypt.hashpw(password.encode(), salt)
    result = run_statement("CALL resto_login(?,?,?)", [email, hash_result, token])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"
    

@app.delete('/api/restaurant-login')
def resto_logout():
    token = request.json.get("token")
    result = run_statement("CALL delete_resto_login(?)", [token])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"