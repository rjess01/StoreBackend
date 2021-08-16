from flask import Flask, render_template
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



if __name__ == '__main__':
    app.run(debug=True)