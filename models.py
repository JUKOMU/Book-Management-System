import random

from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy, SignallingSession, get_state
from sqlalchemy import orm

from config import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


class RoutingSession(SignallingSession):
    """The signalling session is the default session that Flask-SQLAlchemy
    uses.  It extends the default session system with bind selection and
    modification tracking.

    If you want to use a different session you can override the
    :meth:`SQLAlchemy.create_session` function.

    . versionadded:: 2.0

    . versionadded:: 2.1
        The `binds` option was added, which allows a session to be joined
        to an external transaction.

    继承SignallingSession， 重写`get_bind` 使其支持读写分离
    """

    def __init__(self, *args, **kwargs):
        super(RoutingSession, self).__init__(*args, **kwargs)

    def get_bind(self, mapper=None, clause=None):
        """Return the engine or connection for a given model or
        table, using the ``__bind_key__`` if it is set.
        """
        # mapper is None if someone tries to just get a connection
        state = get_state(self.app)
        if mapper is not None:
            try:
                # SA >= 1.3
                persist_selectable = mapper.persist_selectable
            except AttributeError:
                # SA < 1.3
                persist_selectable = mapper.mapped_table

            info = getattr(persist_selectable, 'info', {})
            bind_key = info.get('bind_key')
            if bind_key is not None:
                return state.db.get_engine(self.app, bind=bind_key)

        # 读写分离
        from sqlalchemy.sql.dml import UpdateBase
        if self._flushing or isinstance(clause, UpdateBase):
            print("user master DB")
            return state.db.get_engine(self.app, bind="master")
        else:
            print("user slave DB")
            return state.db.get_engine(self.app, bind=random.choice(list(app.config["SQLALCHEMY_BINDS"].keys())))


class RoutingSQLAlchemy(SQLAlchemy):
    """
    重写 `create_session` 使其使用`RoutingSession`
    """

    def create_session(self, options):
        """Create the session factory used by :meth:`create_scoped_session`.

        The factory **must** return an object that SQLAlchemy recognizes as a session,
        or registering session events may raise an exception.

        Valid factories include a :class:`~sqlalchemy.orm.session.Session`
        class or a :class:`~sqlalchemy.orm.session.sessionmaker`.

        The default implementation creates a ``sessionmaker`` for :class:`RoutingSession`.

        :param options: dict of keyword arguments passed to session class
        """

        return orm.sessionmaker(class_=RoutingSession, db=self, **options)


db = RoutingSQLAlchemy(app)


class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.String(6), primary_key=True)
    admin_name = db.Column(db.String(32))
    password = db.Column(db.String(24))
    right_col = db.Column(db.String(32))
    avatar = db.Column(db.Boolean, default=False)

    def __init__(self, admin_id, admin_name, password, right_col, avatar):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.password = password
        self.right_col = right_col
        self.avatar = avatar

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
    avatar = db.Column(db.Boolean, default=False)  # 头像

    def __init__(self, card_id, student_id, password, student_name, sex, telephone, enroll_date, valid_date, loss=False,
                 debt=False, avatar=False):
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
        self.avatar = avatar

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
    student_name = db.Column(db.String(32))
    comment = db.Column(db.String(10240))
    date = db.Column(db.String(13))  # 日期
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Comments %r>' % self.id


class CommentsAdmin(db.Model):
    __tablename__ = 'comments_admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment_id = db.Column(db.String(10))
    admin_id = db.Column(db.String(10))
    name = db.Column(db.String(255))
    comment = db.Column(db.String(1024))
    date = db.Column(db.String(13))  # 日期

    def to_dict(self):
        return {
            'id': self.id,
            'comment_id': self.comment_id,
            'admin_id': self.admin_id,
            'name': self.name,
            'comment': self.comment,
            'date': self.date
        }

    def __repr__(self):
        return '<CommentsAdmin %r>' % self.id


class Announcements(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    date = db.Column(db.String(13))  # 日期

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date
        }

    def __repr__(self):
        return '<Announcements %r>' % self.id


class CommentsStudent(db.Model):
    __tablename__ = 'comments_student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment_id = db.Column(db.String(10))
    student_id = db.Column(db.String(10))
    name = db.Column(db.String(255))
    comment = db.Column(db.String(1024))
    date = db.Column(db.String(13))  # 日期

    def to_dict(self):
        return {
            'id': self.id,
            'comment_id': self.comment_id,
            'student_id': self.student_id,
            'name': self.name,
            'comment': self.comment,
            'date': self.date
        }

    def __repr__(self):
        return '<CommentsStudent %r>' % self.id
