from flask import Flask, request, make_response, jsonify
from dbcreds import production_mode
import json
# importing from the flder client, file client.py as c
import client.client as c

app = Flask(__name__)


#!..................CLIENT......................
"""Importing all the fucntions from the client.py"""

@app.get('/api/client')
def client_get():
    return c.get_client()


@app.post('/api/client')
def post_client():
    return c.post_client()


@app.patch('/api/client')
def patch_client():
    return c.patch_client()

@app.delete('/api/client')
def delete_client():
    return c.delete_client()



#!..................RESTAURANT......................








if (production_mode == True):
    print("Running server in prductioin mode")
    import bjoern #type:ignore
    bjoern.run(app, "0.0.0.0", 5000)
    # NON-production case
else:
    print("Running testing mode")
    # adding CROS so it will accept requests from different origins
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)