from flask import request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app
#*Importing app from app as only a single app object is allowed

# !NEED UUID, WILL COME BACK LATER

@app.get('/api/client-login')
def client_login():
    client_id = request.json.get("userId")
    token = request.json.get("token")
    result = run_statement("CALL post_client_session(?,?)", [client_id, token])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"