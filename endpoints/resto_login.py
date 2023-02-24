from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app
#*Importing app from app as only a single app object is allowed

@app.post('/api/restaurant-login')
def resto_login():
    resto_id = request.json.get("restoId")
    token = request.json.get("token")
    result = run_statement("CALL post_resto_session(?,?)", [resto_id, token])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"