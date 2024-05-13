from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.String(6), primary_key=True)
    admin_name = db.Column(db.String(32))
    password = db.Column(db.String(24))
    right_col = db.Column(db.String(32))

    def __init__(self, admin_id, admin_name, password, right_col):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.password = password
        self.right_col = right_col

    def get_id(self):
        return self.admin_id

    def verify_password(self, password):
        if password == self.password:
            return True
        else:
            return False

    def __repr__(self):
        return '<Admin %r>' % self.admin_name


class Student(UserMixin, db.Model):
    __tablename__ = 'student'
    card_id = db.Column(db.String(8), primary_key=True)
    student_id = db.Column(db.String(9))
    password = db.Column(db.String(24))
    student_name = db.Column(db.String(32))
    sex = db.Column(db.String(2))
    telephone = db.Column(db.String(11), nullable=True)
    enroll_date = db.Column(db.String(13))
    valid_date = db.Column(db.String(13))
    loss = db.Column(db.Boolean, default=False)  # 是否挂失
    debt = db.Column(db.Boolean, default=False)  # 是否欠费

    def __init__(self, card_id, student_id, password, student_name, sex, telephone, enroll_date, valid_date, loss=False,
                 debt=False):
        self.card_id = card_id
        self.student_id = student_id
        self.password = password
        self.student_name = student_name
        self.sex = sex
        self.telephone = telephone
        self.enroll_date = enroll_date
        self.valid_date = valid_date
        self.loss = loss
        self.debt = debt

    def get_id(self):
        return self.card_id

    def verify_password(self, password):
        if password == self.password:
            return True
        else:
            return False

    def __repr__(self):
        return '<Student %r>' % self.student_name


class Book(db.Model):
    __tablename__ = 'book'
    isbn = db.Column(db.String(13), primary_key=True)
    book_name = db.Column(db.String(64))
    author = db.Column(db.String(64))
    press = db.Column(db.String(32))
    class_name = db.Column(db.String(64))

    def __repr__(self):
        return '<Book %r>' % self.book_name


class Inventory(db.Model):
    __tablename__ = 'inventory'
    barcode = db.Column(db.String(6), primary_key=True)
    isbn = db.Column(db.ForeignKey('book.isbn'))
    storage_date = db.Column(db.String(13))
    location = db.Column(db.String(32))
    withdraw = db.Column(db.Boolean, default=False)  # 是否注销
    status = db.Column(db.Boolean, default=True)  # 是否在馆
    admin = db.Column(db.ForeignKey('admin.admin_id'))  # 入库操作员

    def __repr__(self):
        return '<Inventory %r>' % self.barcode


class ReadBook(db.Model):
    __tablename__ = 'readbook'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barcode = db.Column(db.ForeignKey('inventory.barcode'), index=True)
    card_id = db.Column(db.ForeignKey('student.card_id'), index=True)
    start_date = db.Column(db.String(13))
    borrow_admin = db.Column(db.ForeignKey('admin.admin_id'))  # 借书操作员
    end_date = db.Column(db.String(13), nullable=True)
    return_admin = db.Column(db.ForeignKey('admin.admin_id'))  # 还书操作员
    due_date = db.Column(db.String(13))  # 应还日期

    def __repr__(self):
        return '<ReadBook %r>' % self.id

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.String(10))
    comment = db.Column(db.String(1024))
    date = db.Column(db.String(13))  # 日期
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Comments %r>' % self.id

