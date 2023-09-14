from flask import Flask, render_template
from leapcell import Leapcell
import pandas as pd
import requests
from io import BytesIO
from PIL import Image
import os

api = Leapcell(
    os.environ.get("LEAPCELL_API_KEY"),
)

table = api.table("salamer/myblog", "tbl1702369503563026432", name_type="name")


app = Flask(__name__)

@app.route("/")
def hello_world():
    records = table.select().query()
    return render_template('index.html', title='Welcome', products=records)

@app.route("/product/<id>")
def product(id):
    item = table.get_by_id(id)
    return render_template('item.html', title='Welcome', product=item)

if __name__ == '__main__':
    app.run(debug=False, port=8000)