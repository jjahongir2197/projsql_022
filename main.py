from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cache.db'
db = SQLAlchemy(app)

cache = {}

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

def get_products():
    if "products" in cache:
        return cache["products"]

    products = Product.query.all()
    cache["products"] = products
    return products

with app.app_context():
    db.create_all()

    db.session.add(Product(name="Phone"))
    db.session.commit()

    print(get_products())
