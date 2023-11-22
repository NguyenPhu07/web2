from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from web22 import db,app
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2



class User(db.Model):
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')

    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name






class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id=Column(Integer, ForeignKey(Category.id), nullable=False)
    def __str__(self):
        return self.name




if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        import hashlib
        u = User(name='Admin', username='admin',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRoleEnum.ADMIN)
        db.session.add(u)
        db.session.commit()



        # # c4 = Category(name='')
        # # c5 = Category(name='Watch')
        # # c6 = Category(name='Sport')
        # # db.session.add(c4)
        # # db.session.add(c5)
        # # db.session.add(c6)
        # # db.session.commit()
        #
        # p1= Product(name='iphone13', price=20000, category_id=1,
        #             image="https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png")
        #
        # p2 = Product(name='Galaxy z fold', price=20000,category_id=1,
        #              image="https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png")
        #
        # p3 = Product(name='Galaxy tabs23', price=20000,category_id=1,
        #              image="https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png")
        #
        # p4 = Product(name='iphone12', price=20000, category_id=1,
        #              image="https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png")
        #
        # p5 = Product(name='Galaxys23', price=20000, category_id=1,
        #              image="https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png")
        #
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
        # #
        #
