from flask import request, make_response, jsonify
from helpers.dbhelpers import run_statement
from app import app

# Get order for client
@app.get('/api/orders')
def get_c_orders():
    c_id_input = request.args.get("clientId")
    o_id_input = request.args.get("orderId")
    orders = run_statement("CALL get_client_orders(?,?)", [c_id_input, o_id_input])
    keys = ["Id", "client_id", "restaurant_id", "is_confirmed" "is_completed", "is_cancelled", "created_at"]
    result = []
    if(type(orders) == list):
        for i in orders:
            zipped = zip(keys, i)
            result.append(dict(zipped))
        return make_response(jsonify(result), 200)
    else:
        return make_response(jsonify(result), 500)
    

# Get orders for resto
@app.get('/api/orders')
def get_r_orders():
    id_input = request.args.get("restoId")
    orders = run_statement("CALL get_resto_orders(?)", [id_input])
    keys = ["Id", "client_id", "restaurant_id", "is_confirmed" "is_completed", "is_cancelled", "created_at"]
    result = []
    if(type(orders) == list):
        for i in orders:
            zipped = zip(keys, i)
            result.append(dict(zipped))
        return make_response(jsonify(result), 200)
        # 200 code is good to get a get request
    else:
        return make_response(jsonify(result), 500)


@app.post('/api/orders')
def post_order():
    o_id = request.json.get("orderId")
    m_id = request.json.get("menuId")
    result = run_statement("CALL post_order(?,?,?)", [o_id, m_id])
    if result == None:
        return make_response(jsonify("Order placed successfully"), 200)
    else:
        return make_response(jsonify(result), 500)

# Patch for client - clients can only cancel order
@app.patch('/api/orders')
def client_patch_order():
    orderID = request.json.get("orderID")
    cancleOrder = request.json.get("cancelOrder")
    result = run_statement("CALL patch_client_order(?,?)", [orderID, cancleOrder])
    if result == None:
        return make_response(jsonify("Order updated Successfully"),200)
    else:
        return make_response(jsonify("Something went wrong!"),500)
    
# Patch for restaurant - resto can only confirm and complete orders
@app.patch('/api/orders')
def resto_patch_order():
    orderID = request.json.get("orderID")
    confirmOrder = request.json.get("confirmOrder")
    completeOrder = request.json.get("completeOrder")
    result = run_statement("CALL patch_resto_order(?,?,?)", [orderID, confirmOrder, completeOrder])
    if result == None:
        return make_response(jsonify("Order updated Successfully"),200)
    else:
        return make_response(jsonify("Something went wrong!"),500)


    
