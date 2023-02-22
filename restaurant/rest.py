from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from dbcreds import production_mode
import client.client as c


app = Flask(__name__)


@app.get('/api/client-login')
def get_restaurant():
    pass
