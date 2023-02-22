from flask import Flask, request, make_response, jsonify
from dbhelpers import run_statement
from dbcreds import production_mode


app = Flask(__name__)


@app.get('/api/client-login')
def get_restaurant():
    client_id = request.json.get("userId")
    token = request.json.get("token")
    result = run_statement("CALL post_client_session(?,?)", [client_id, token])
    if result == None:
        return "All good"
    else:
        return "Some went wrong!"