from flask import render_template, request
import dao
from web22 import app


@app.route("/")
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    mssg = dao.get_products(kw)
    return render_template('index.html', categories=cates, products=mssg)
    #caterories, products la tham so de doi chieu qua index.html


if __name__ == '__main__':
    app.run(debug=True)
