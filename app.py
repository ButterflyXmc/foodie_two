from flask import Flask, request, make_response, jsonify
from dbhelpers import run_statement
from dbcreds import production_mode

app = Flask(__name__)


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
    result = run_statement("CALL post_client(?,?,?,?,?)", [username, first_name, last_name, email, password])
    if result == None:
        return "All good"
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