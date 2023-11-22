from flask import render_template, request
import dao
from web22 import app, login


@app.route("/")
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    products = dao.get_products(kw)
    return render_template('index.html', categories=cates, products=products)
    #caterories, products la tham so de doi chieu qua index.html

@app.route('/admin/login', methods=['post'])
def admin_login():
    request.form.get('username')
    request.form.get('password')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    from web22 import admin
    app.run(debug=True)
