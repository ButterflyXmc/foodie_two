from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from dbcreds import production_mode
from app import app
import bcrypt
#*Importing app from app as only a single app object is allowed


@app.get('/api/restaurant')
def get_resto():
    id_input = request.args.get("restoId")
    get_resto = run_statement("CALL get_resto(?)", [id_input])
    keys = ["Id", "name", "address", "city", "email", "phone_num", "password", "bio", "banner_url", "profile_url"]
    result = []
    if(type(get_resto) == list):
        for i in get_resto:
            zipped = zip(keys, i)
            result.append(dict(zipped))
        return make_response(jsonify(result), 200)
        # 200 code is good to get a get request
    else:
        return make_response(jsonify(result), 500)


@app.post('/api/restaurant')
def post_resto():
    name = request.json.get("restoName")
    address = request.json.get("restoAddress")
    city = request.json.get("city")
    email = request.json.get("email")
    phone_num = request.json.get("phoneNum")
    password = request.json.get("password")
    salt = bcrypt.gensalt()
    hash_result = bcrypt.hashpw(password.encode(), salt)
    bio = request.json.get("bio")
    result = run_statement("CALL post_resto(?,?,?,?,?,?,?)", [name, address, city, email, phone_num, hash_result, bio])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"
    

@app.patch('/api/restaurant')
def patch_resto():
    id = request.json.get('restoId')
    name = request.json.get('restoName')
    address = request.json.get('restoAddress')
    city = request.json.get('restoCity')
    email = request.json.get('restoEmail')
    phone_num = request.json.get('phoneNum')
    password = request.json.get('password')
    bio = request.json.get('bio')
    banner_url = request.json.get('bannerUrl')
    profile_url = request.json.get('profileUrl')
    result = run_statement("CALL patch_resto(?,?,?,?,?,?,?,?,?,?", [id, name, address, city, email, phone_num, password, bio, banner_url, profile_url])
    if result == None:
        return make_response(jsonify("Post updated Successfully"),200)
    else:
        return make_response(jsonify("Something went wrong!"),500)
