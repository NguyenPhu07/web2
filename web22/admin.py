from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from web22.models import Category, Product
from web22 import app,db
admin = Admin(app=app, name='Quan tri ban hang', template_mode='bootstrap4')
class MyProductView(ModelView):
   column_list = ['id','name','price']
   can_export = True
   column_searchable_list = ['name']
   column_filters = ['name','price']
   column_editable_list = ['name','price']
   edit_modal = True


class MyCategory(ModelView):
   column_list = ['name','products']

class MyStasView(BaseView):
   @expose("/")
   def index(self):
      return self.render('admin/stats.html')



admin.add_view(MyCategory(Category,db.session))
admin.add_view( MyProductView(Product,db.session))
admin.add_view(MyStasView(name='Thống kê báo cáo'))