from dbcreds import production_mode
from flask_cors import CORS
from app import app

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