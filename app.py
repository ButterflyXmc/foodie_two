from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from dbcreds import production_mode
# & Importing file client.py from client folder as c
import client.client as c

app = Flask(__name__)

# !............................CLIENT...........................
# Each functions returns diff functions from client.py
@app.get('/api/client')
def get():
    return c.get_client()

@app.post('/api/client')
def post():
    return c.post_client()

@app.get('/api/client')
def patch():
    return c.patch_client()

@app.get('/api/client')
def delete():
    return c.delete_client()





    # app.run(debug = True)
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