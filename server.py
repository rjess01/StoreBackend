from flask import Flask, render_template, abort, request
import json
from data import data
app = Flask(__name__) # create a flask app

me = {
    "name": "Jesse",
    "last_name": "Ramos",
    "age": 23,
    "email": "jesser@hotmail.com",
    "address": {
        "street": "simp ave",
        "number": 3
    }
}



@app.route('/')
@app.route('/home')
def home_page():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return me["name"] + " " + me["last_name"]


# /about/email

@app.route("/about/email")
def about_me_email():
    return me["email"]






@app.route("/api/catalog")
def get_catalog():
    return json.dumps(data)


@app.route("/api/catalog", methods=['POST'])
def save_product():
    product = request.get_json() #returns dict
    data.append(product)

    return json.dumps(product)


@app.route("/api/catagories")
def get_catagories():
    """
     Get the unique catagories from the catalog (data var)
     and returen them as a list of string 
    """

    categories = []
    for item in data:
        cat = item["category"]

        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)


# get /api/catalog/id/<id>
# get a product by its _id
@app.route("/api/catalog/id/<id>")
def get_product_by_id(id):
    """
    look in your data list
    for a dictionary with the _id equal to id param
     return it as a json or return an error if not found
    """
    for item in data:
        if(str(item["_id"]) == id):
            return json.dumps(item)

    abort(404)
    
# /api/catalog/category/<catagory>
# get all the products that belong to recived category

@app.route("/api/catalog/category/<category>")
def get_products_by_category(category):
    results = []
    for item in data:
        if(item["category"].lower() == category.lower()):
            results.append(item)

    return json.dumps(results)


@app.route("/api/catalog/cheapest")
def get_cheapest():
    cheapest = data[0]
    for item in data:
        if(item["price"] < cheapest["price"]):
            cheapest = item


    return json.dumps(cheapest)





if __name__ == '__main__':
    app.run(debug=True)