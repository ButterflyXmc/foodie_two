from flask import request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app

@app.get('/api/orders')
def get_orders():
    id_input = request.args.get("orderId")
    orders = run_statement("CALL get_orders(?)", [id_input])
    keys = ["Id", "client_id", "restaurant_id", "is_confirmed" "is_completed", "is_cancelled", "created_at", "items"]
    result = []
    if(type(orders) == list):
        for i in orders:
            zipped = zip(keys, i)
            result.append(dict(zipped))
        return make_response(jsonify(result), 200)
        # 200 code is good to get a get request
    else:
        return make_response(jsonify(result), 500)


@app.get('/api/orders')
def post_order():
    client_id = request.json.get("clientId")
    resto_id = request.json.get("restoId")
    items = request.json.get("items")
    result = run_statement("CALL post_order(?,?,?)", [client_id, resto_id, items])
    if (type(result)== list):
        if result == []:
            return make_response(jsonify("Please try again!"), 500)
    else:
        return "Some went wrong!"
    

# Patch for client - clients can only cancel order
@app.patch('/api/orders')
def client_patch_order():
    orderID = request.json.get("orderID")
    cancleOrder = request.json.get("cancelOrder")
    result = run_statement("CALL patch_client_order(?,?)", [orderID, cancleOrder])
    if (type(result)== list):
        if result == []:
            return make_response(jsonify("Please try again!"), 500)
    else:
        return "Some went wrong!"
    
# Patch for restaurant - resto can only confirm and complete orders
@app.patch('/api/orders')
def resto_patch_order():
    orderID = request.json.get("orderID")
    confirmOrder = request.json.get("confirmOrder")
    completeOrder = request.json.get("completeOrder")
    result = run_statement("CALL patch_resto_order(?,?,?)", [orderID, confirmOrder, completeOrder])
    if (type(result)== list):
        if result == []:
            return make_response(jsonify("Please try again!"), 500)
    else:
        return "Some went wrong!"


    
