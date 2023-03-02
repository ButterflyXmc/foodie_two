from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from dbcreds import production_mode
from app import app
import bcrypt
import uuid
#Importing app from app as only a single app object is allowed

@app.get('/api/client')
def get_client():
    id_input = request.args.get("userId")
    get_client = run_statement("CALL get_client(?)", [id_input])
    keys = ["Id", "username", "first_name", "last_name", "email", "password", "created_at"]
    result = []
    if(type(get_client) == list):
        for client in get_client:
            zipped = zip(keys, client)
            result.append(dict(zipped))
        return make_response(jsonify(result), 200)
        # 200 code is good to get a get request
    else:
        return make_response(jsonify(result), 500)


@app.post('/api/client')
def post_client():
    username = request.json.get("userName")
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    password = request.json.get("password")
    salt = bcrypt.gensalt()
    hash_result = bcrypt.hashpw(password.encode(), salt)
    result = run_statement("CALL post_client(?,?,?,?,?)", [username, first_name, last_name, email, hash_result])
    if (type(result)== list):
        if result == []:
            return make_response(jsonify("Please try again!"), 500)
    else:
        return "Some went wrong!"
    

@app.patch('/api/client')
def patch_client():
    id = request.json.get('userId')
    username = request.json.get('userName')
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    result = run_statement("CALL patch_client(?,?,?,?,?,?)", [id, username, first_name, last_name, email, password])
    if result == None:
        return make_response(jsonify("Post updated Successfully"),200)
    else:
        return make_response(jsonify("Something went wrong!"),500)


@app.delete('/api/client')
def delete_client():
    id = request.json.get("userId")
    if id == None:
        return "You must enter a valid user ID"
    result = run_statement("CALL delete_client(?)", [id])
    if result == None:
        return make_response(jsonify("Post deleted Successfully"),200)
    else:
        return make_response(jsonify("Something went wrong!"), 500)
