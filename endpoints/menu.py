from flask import Flask, request, make_response, jsonify
from helpers.dbhelpers import run_statement
from dbcreds import production_mode
from app import app
#*Importing app from app as only a single app object is allowed

# Doesnt take any args as the menu should be visible to both the resto and the client as per Mark
@app.get('/api/menu')
def get_menu():
    menu_get = run_statement("CALL get_menu()")
    keys = ["ItemId", "RestaurantId" "Name", "Description", "Price", "Image_url"]
    result =[]
    if(type(result) == list):
        for menu in menu_get:
            zipped = zip(keys, menu)
            result.append(dict(zipped))
        return make_response(jsonify(result), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)
    

@app.post('/api/menu')
def post_menu():
    name = request.json.get("itemName")
    description = request.json.get("description")
    price = request.json.get("price")
    restaurant_id = request.json.get("restoId")
    result = run_statement("CALL post_menu(?,?,?,?)", [name, description, price, restaurant_id])
    if result == None:
        return make_response(jsonify("Item added successfully"), 200)
    else:
        return make_response(jsonify(result), 500)
    

@app.patch('/api/menu')
def patch_menu():
    id = request.json.get("itemId")
    name = request.json.get("itemName")
    description = request.json.get("description")
    price = request.json.get("price")
    img = request.json.get("imgUrl")
    result = run_statement("CALL patch_menu(?,?,?,?,?)", [id, name, description, price, img])
    if result == None:
        return make_response(jsonify("Menu updated Successfully"),200)
    else:
        return make_response(jsonify("Something went wrong!"),500)
    

@app.delete('/api/menu')
def delete_menu():
    id = request.json.get("itemId")
    result = run_statement("CALL delete_menu(?)", [id])
    if result == None:
        return make_response(jsonify("Account deleted Successfully"),200)
    else:
        return make_response(jsonify("Something went wrong!"), 500)
    
