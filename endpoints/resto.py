from flask import request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app
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

