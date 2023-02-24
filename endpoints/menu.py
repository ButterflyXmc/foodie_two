from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from dbcreds import production_mode
from app import app
#*Importing app from app as only a single app object is allowed

@app.get('/api/menu')
def get_menu():
    pass