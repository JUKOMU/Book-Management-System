import datetime
import json
import time
import random
import os
import requests
from flask import Flask, request, jsonify, Response
from flask import render_template, session, redirect, url_for, flash, make_response
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from forms import Login, SearchBookForm, ChangePasswordForm, EditInfoFormAdmin, EditInfoFormStudent, SearchStudentForm, \
    NewStoreForm, StoreForm, BorrowForm, WriteOffForm, AnnouncementForm
from models import *


# 配置 CORS，允许所有域名跨域
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.shell_context_processor
def make_shell_context():
    return {
        'app': app,
        'db': db,
        'admin': admin,
        'student': student,
        'Book': Book  # 你需要替换为你的 Book 模型类
    }


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'basic'
login_manager.login_view = 'login'
login_manager.login_message = u"请先登录。"


@login_manager.user_loader
def load_user(user_id):
    if len(user_id) == 6:
        return Admin.query.get(int(user_id))
    else:
        return Student.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    isUser = False
    form = Login()
    if form.validate_on_submit():
        account_id = form.account.data
        password = form.password.data

        # 根据账号长度判断是管理员还是学生
        if len(account_id) == 6:
            user = Admin.query.filter_by(admin_id=account_id, password=password).first()
            # 创建响应对象
            response = make_response(redirect(url_for('index_admin')))
        elif len(account_id) == 8 or len(account_id) == 4:
            isUser = True
            user = Student.query.filter_by(card_id=account_id, password=password).first()
            response = make_response(redirect(url_for('index_student')))
        else:
            user = None

        if user is None:
            flash('账号或密码错误！')
            return redirect(url_for('login'))
        else:
            if isUser:
                login_user(user)
                session['id'] = user.card_id
                session['name'] = user.student_name
            else:
                login_user(user)
                session['id'] = user.admin_id
                session['name'] = user.admin_name

            # 根据用户类型存储 admin_id 或 card_id 到 cookie
            if isinstance(user, Admin):
                response.set_cookie('admin_id', str(user.admin_id))
            elif isinstance(user, Student):
                response.set_cookie('card_id', str(user.card_id))
                response.set_cookie('loss', str(user.loss))

            # 返回响应对象，包含设置的 cookie
            return response
    return render_template('login.html', form=form)


# def login():
#     form = Login()
#     if form.validate_on_submit():
#         user = Admin.query.filter_by(admin_id=form.account.data, password=form.password.data).first()
#         if user is None:
#             flash('账号或密码错误！')
#             return redirect(url_for('login'))
#         else:
#             # 登录用户
#             login_user(user)
#
#             # 创建响应对象
#             response = make_response(redirect(url_for('index_admin')))
#
#             # 将 admin_id 存入 cookie
#             response.set_cookie('admin_id', str(user.admin_id))
#
#             # 返回响应对象，包含设置的 cookie
#             return response
#     return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经登出！')
    return redirect(url_for('login'))


@app.route('/index_admin')
@login_required
def index_admin():
    return render_template('admin/index-admin.html', name=session.get('name'))


@app.route('/index_student')
@login_required
def index_student():
    return render_template('student/index-student.html', name=session.get('name'))


@app.route('/echarts')
@login_required
def echarts():
    days = []
    num = []
    today_date = datetime.date.today()
    today_str = today_date.strftime("%Y-%m-%d")
    today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
    ten_ago = int(today_stamp) - 9 * 86400
    for i in range(0, 10):
        borr = ReadBook.query.filter_by(start_date=str((ten_ago + i * 86400) * 1000)).count()
        retu = ReadBook.query.filter_by(end_date=str((ten_ago + i * 86400) * 1000)).count()
        num.append(borr + retu)
        days.append(timeStamp((ten_ago + i * 86400) * 1000))
    data = []
    for i in range(0, 10):
        item = {'name': days[i], 'num': num[i]}
        data.append(item)
    return jsonify(data)


@app.route('/user/<id>')
@login_required
def user_info_admin(id):
    user = Admin.query.filter_by(admin_id=id).first()
    return render_template('admin/user-info_admin.html', user=user, name=session.get('name'))


@app.route('/user1/<id>')
def user_info_student(id):
    user = Student.query.filter_by(card_id=id).first()
    valid_date = timeStamp(current_user.valid_date)
    enroll_date = timeStamp(current_user.enroll_date)
    return render_template('student/user-info_student.html', user=user, name=session.get('name'), valid_date=valid_date,
                           enroll_date=enroll_date)


@app.route('/change_password_admin', methods=['GET', 'POST'])
@login_required
def change_password_admin():
    form = ChangePasswordForm()
    if form.password2.data != form.password.data:
        flash(u'两次密码不一致！')
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash(u'已成功修改密码！')
            return redirect(url_for('index_admin'))
        else:
            flash(u'原密码输入错误，修改失败！')
    return render_template("admin/change-password_admin.html", form=form)


@app.route('/change_password_student', methods=['GET', 'POST'])
@login_required
def change_password_student():
    form = ChangePasswordForm()
    if form.password2.data != form.password.data:
        flash(u'两次密码不一致！')
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash(u'已成功修改密码！')
            return redirect(url_for('index_admin'))
        else:
            flash(u'原密码输入错误，修改失败！')
    return render_template("student/change-password_student.html", form=form)


@app.route('/change_info_admin', methods=['GET', 'POST'])
@login_required
def change_info_admin():
    form = EditInfoFormAdmin()
    if form.is_submitted():
        current_user.admin_name = form.name.data
        db.session.add(current_user)
        # 提交修改
        db.session.commit()
        flash(u'已成功修改个人信息！')
        # base页面刷新信息
        session['name'] = current_user.admin_name
        return redirect(url_for('user_info_admin', id=current_user.admin_id))
    form.name.data = current_user.admin_name
    id = current_user.admin_id
    right = current_user.right_col
    return render_template('admin/change-info_admin.html', form=form, id=id, right=right)


# 写学生change-info功能
@app.route('/change_info_student', methods=['GET', 'POST'])
@login_required
def change_info_student():
    form = EditInfoFormStudent()
    if form.is_submitted():
        print(current_user.student_name)
        current_user.student_name = form.name.data
        current_user.sex = form.sex.data
        current_user.telephone = form.telephone.data
        db.session.add(current_user)
        # 提交修改
        db.session.commit()
        flash(u'已成功修改个人信息！')
        # base页面刷新信息
        session['name'] = current_user.student_name
        return redirect(url_for('user_info_student', id=current_user.card_id))
    form.name.data = current_user.student_name
    form.sex.data = current_user.sex
    form.telephone.data = current_user.telephone
    id = current_user.card_id
    valid_date = timeStamp(current_user.valid_date)
    return render_template('student/change-info-student.html', form=form, id=id, valid_date=valid_date)


@app.route('/search_book_admin', methods=['GET', 'POST'])
@login_required
def search_book_admin():  # 这个函数里不再处理提交按钮，使用Ajax局部刷新
    form = SearchBookForm()
    return render_template('admin/search-book_admin.html', name=session.get('name'), form=form)


@app.route('/search_book_student', methods=['GET', 'POST'])
@login_required
def search_book_student():  # 这个函数里不再处理提交按钮，使用Ajax局部刷新
    form = SearchBookForm()
    return render_template('student/search-book_student.html', name=session.get('name'), form=form)


@app.route('/recommend', methods=['GET', 'POST'])
@login_required
def recommend():
    return render_template('student/recommend.html', name=session.get('name'))


@app.route('/books', methods=['POST'])
def find_book():
    def find_name():
        content = request.form.get('content', '').strip()
        if not content:
            return Book.query.all()
        else:
            return Book.query.filter(Book.book_name.like('%' + content + '%')).all()

    def find_author():
        content = request.form.get('content', '').strip()
        if not content:
            return Book.query.all()
        else:
            return Book.query.filter(Book.author.contains(content)).all()

    def find_class():
        content = request.form.get('content', '').strip()
        if not content:
            return Book.query.all()
        else:
            return Book.query.filter(Book.class_name.contains(content)).all()

    def find_isbn():
        content = request.form.get('content', '').strip()
        if not content:
            return Book.query.all()
        else:
            return Book.query.filter(Book.isbn.contains(content)).all()

    methods = {
        'book_name': find_name,
        'author': find_author,
        'class_name': find_class,
        'isbn': find_isbn
    }
    books = methods[request.form.get('method')]()
    data = []
    for book in books:
        count = Inventory.query.filter_by(isbn=book.isbn).count()
        available = Inventory.query.filter_by(isbn=book.isbn, status=True).count()
        item = {'isbn': book.isbn, 'book_name': book.book_name, 'press': book.press, 'author': book.author,
                'class_name': book.class_name, 'count': count, 'available': available}
        data.append(item)
    return jsonify(data)


@app.route('/user/book', methods=['GET', 'POST'])
def user_book():
    form = SearchBookForm()
    return render_template('user-book.html', form=form)


@app.route('/search_student', methods=['GET', 'POST'])
@login_required
def search_student():
    form = SearchStudentForm()
    return render_template('admin/search-student.html', name=session.get('name'), form=form)


def timeStamp(timeNum):
    if timeNum is None:
        return timeNum
    else:
        timeStamp = float(float(timeNum) / 1000)
        timeArray = time.localtime(timeStamp)
        print(time.strftime("%Y-%m-%d", timeArray))
        return time.strftime("%Y-%m-%d", timeArray)


@app.route('/student', methods=['POST'])
def find_student():
    stu = Student.query.filter_by(card_id=request.form.get('card')).first()
    if stu is None:
        return jsonify([])
    else:
        valid_date = timeStamp(stu.valid_date)
        return jsonify([{'name': stu.student_name, 'gender': stu.sex, 'valid_date': valid_date, 'debt': stu.debt}])


@app.route('/record', methods=['POST'])
def find_record():
    records = db.session.query(ReadBook).join(Inventory).join(Book).filter(ReadBook.card_id == request.form.get('card')) \
        .with_entities(ReadBook.barcode, Inventory.isbn, Book.book_name, Book.author, ReadBook.start_date,
                       ReadBook.end_date, ReadBook.due_date).all()

    data = []
    for record in records:
        start_date = timeStamp(record.start_date)
        due_date = timeStamp(record.due_date)
        end_date = timeStamp(record.end_date)
        if end_date is None:
            end_date = '未归还'
        item = {'barcode': record.barcode, 'book_name': record.book_name, 'author': record.author,
                'start_date': start_date, 'due_date': due_date, 'end_date': end_date}
        data.append(item)
    return jsonify(data)


@app.route('/user/student', methods=['GET', 'POST'])
def user_student():
    form = SearchStudentForm()
    return render_template('user-student.html', form=form)


@app.route('/writeOff', methods=['GET', 'POST'])
@login_required
def write_off():
    if request.method == 'POST':
        # 处理注销书籍的请求
        data = request.json
        barcode = data.get('barcode')
        inventory = Inventory.query.filter_by(barcode=barcode).first()
        if inventory:
            db.session.delete(inventory)
            db.session.commit()
            return jsonify({'status': 'success', 'message': '注销成功！'})
        else:
            return jsonify({'status': 'failure', 'message': '注销失败，未找到对应的图书信息。'}), 404

    # 获取所有书籍的信息
    books = Book.query.all()
    inventorys = Inventory.query.all()

    return render_template('admin/write_off.html', books=books, inventorys=inventorys, name=session.get('name'))


@app.route('/storage', methods=['GET', 'POST'])
@login_required
def storage():
    form = StoreForm()
    if form.validate_on_submit():
        book = Book.query.filter_by(isbn=request.form.get('isbn')).first()
        exist = Inventory.query.filter_by(barcode=request.form.get('barcode')).first()
        if book is None:
            flash(u'添加失败，请注意本书信息是否已录入，若未登记，请在‘新书入库’窗口录入信息。')
        else:
            if len(request.form.get('barcode')) != 6:
                flash(u'图书编码长度错误')
            else:
                if exist is not None:
                    flash(u'该编号已经存在！')
                else:
                    num = request.form.get('num')
                    num = int(num)
                    while (num > 0):
                        item = Inventory()
                        item.barcode = str(random.randint(100000, 999999))
                        item.isbn = request.form.get('isbn')
                        item.admin = current_user.admin_id
                        item.location = request.form.get('location')
                        item.status = True
                        item.withdraw = False
                        today_date = datetime.date.today()
                        today_str = today_date.strftime("%Y-%m-%d")
                        today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
                        item.storage_date = int(today_stamp) * 1000
                        db.session.add(item)
                        db.session.commit()
                        num -= 1
                    flash(u'入库成功！')
        return redirect(url_for('storage'))
    return render_template('admin/storage.html', name=session.get('name'), form=form)


@app.route('/new_store', methods=['GET', 'POST'])
@login_required
def new_store():
    form = NewStoreForm()
    if form.validate_on_submit():
        if len(request.form.get('isbn')) != 13:
            flash(u'ISBN长度错误')
        else:
            exist = Book.query.filter_by(isbn=request.form.get('isbn')).first()
            if exist is not None:
                flash(u'该图书信息已经存在，请核对后再录入；或者填写入库表。')
            else:
                book = Book()
                book.isbn = request.form.get('isbn')
                book.book_name = request.form.get('book_name')
                book.press = request.form.get('press')
                book.author = request.form.get('author')
                book.class_name = request.form.get('class_name')
                db.session.add(book)
                db.session.commit()
                flash(u'图书信息添加成功！')
        return redirect(url_for('new_store'))
    return render_template('admin/new-store.html', name=session.get('name'), form=form)


@app.route('/borrow_admin', methods=['GET', 'POST'])
@login_required
def borrow_admin():
    form = BorrowForm()
    books = Book.query.all()
    inventorys = Inventory.query.all()
    return render_template('admin/borrow-admin.html', name=session.get('name'), form=form, books=books,
                           inventorys=inventorys)


@app.route('/borrow_student', methods=['GET', 'POST'])
@login_required
def borrow_student():
    form = BorrowForm()
    books = Book.query.all()
    inventorys = Inventory.query.all()
    id = current_user.card_id
    return render_template('student/borrow-student.html', name=session.get('name'), form=form, id=id, books=books,
                           inventorys=inventorys)


@app.route('/find_stu_book', methods=['GET', 'POST'])
def find_stu_book():
    stu = Student.query.filter_by(card_id=request.form.get('card')).first()
    today_date = datetime.date.today()
    today_str = today_date.strftime("%Y-%m-%d")
    today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
    if stu is None:
        return jsonify([{'stu': 0}])  # 没找到
    if stu.debt is True:
        return jsonify([{'stu': 1}])  # 欠费
    if int(stu.valid_date) < int(today_stamp) * 1000:
        return jsonify([{'stu': 2}])  # 到期
    if stu.loss is True:
        return jsonify([{'stu': 3}])  # 已经挂失
    books = (db.session.query(Book).join(Inventory).
             filter(Book.book_name.contains(request.form.get('book_name')), Inventory.status == 1).
             with_entities(Inventory.barcode, Book.isbn, Book.book_name, Book.author, Book.press).all())
    data = []
    for book in books:
        item = {'barcode': book.barcode, 'isbn': book.isbn, 'book_name': book.book_name,
                'author': book.author, 'press': book.press}
        data.append(item)
    return jsonify(data)


@app.route('/out', methods=['GET', 'POST'])
@login_required
def out():
    today_date = datetime.date.today()
    today_str = today_date.strftime("%Y-%m-%d")
    today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
    barcode = request.args.get('barcode')
    card = request.args.get('card')
    book_name = request.args.get('book_name')
    readbook = ReadBook()
    readbook.barcode = barcode
    readbook.card_id = card
    readbook.start_date = int(today_stamp) * 1000
    readbook.due_date = (int(today_stamp) + 40 * 86400) * 1000
    if type(current_user) is Admin:
        readbook.borrow_admin = current_user.admin_id
    else:
        readbook.borrow_admin = current_user.student_id
    db.session.add(readbook)
    db.session.commit()
    book = Inventory.query.filter_by(barcode=barcode).first()
    book.status = False
    db.session.add(book)
    db.session.commit()
    bks = db.session.query(Book).join(Inventory).filter(Book.book_name.contains(book_name), Inventory.status == 1). \
        with_entities(Inventory.barcode, Book.isbn, Book.book_name, Book.author, Book.press).all()
    data = []
    for bk in bks:
        item = {'barcode': bk.barcode, 'isbn': bk.isbn, 'book_name': bk.book_name,
                'author': bk.author, 'press': bk.press}
        data.append(item)
    return jsonify(data)


@app.route('/return_admin', methods=['GET', 'POST'])
@login_required
def return_book_admin():
    form = SearchStudentForm()
    return render_template('admin/return-admin.html', name=session.get('name'), form=form)


@app.route('/return_student', methods=['GET', 'POST'])
@login_required
def return_book_student():
    card_id = current_user.card_id
    form = SearchStudentForm()
    return render_template('student/return-student.html', name=session.get('name'), form=form, card_id=card_id)


@app.route('/find_not_return_book', methods=['GET', 'POST'])
def find_not_return_book():
    stu = Student.query.filter_by(card_id=request.form.get('card')).first()
    today_date = datetime.date.today()
    today_str = today_date.strftime("%Y-%m-%d")
    today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
    if stu is None:
        return jsonify([{'stu': 0}])  # 没找到
    if stu.debt is True:
        return jsonify([{'stu': 1}])  # 欠费
    if int(stu.valid_date) < int(today_stamp) * 1000:
        return jsonify([{'stu': 2}])  # 到期
    if stu.loss is True:
        return jsonify([{'stu': 3}])  # 已经挂失
    books = (db.session.query(ReadBook).join(Inventory).join(Book).
             filter(ReadBook.card_id == request.form.get('card'), ReadBook.end_date.is_(None)).
             with_entities(ReadBook.barcode, Book.isbn, Book.book_name, ReadBook.start_date, ReadBook.due_date).all())
    data = []
    for book in books:
        start_date = timeStamp(book.start_date)
        due_date = timeStamp(book.due_date)
        item = {'barcode': book.barcode, 'isbn': book.isbn, 'book_name': book.book_name,
                'start_date': start_date, 'due_date': due_date}
        data.append(item)
    return jsonify(data)


@app.route('/in', methods=['GET', 'POST'])
@login_required
def bookin():
    barcode = request.args.get('barcode')
    card = request.args.get('card')
    record = ReadBook.query.filter(ReadBook.barcode == barcode, ReadBook.card_id == card, ReadBook.end_date.is_(None)). \
        first()
    today_date = datetime.date.today()
    today_str = today_date.strftime("%Y-%m-%d")
    today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
    record.end_date = int(today_stamp) * 1000
    if type(current_user) is Admin:
        record.return_admin = current_user.admin_id
    else:
        record.return_admin = current_user.student_id
    db.session.add(record)
    db.session.commit()
    book = Inventory.query.filter_by(barcode=barcode).first()
    book.status = True
    db.session.add(book)
    db.session.commit()
    bks = (db.session.query(ReadBook).join(Inventory).join(Book).
           filter(ReadBook.card_id == card, ReadBook.end_date.is_(None)).
           with_entities(ReadBook.barcode, Book.isbn, Book.book_name, ReadBook.start_date, ReadBook.due_date).all())
    data = []
    for bk in bks:
        start_date = timeStamp(bk.start_date)
        due_date = timeStamp(bk.due_date)
        item = {'barcode': bk.barcode, 'isbn': bk.isbn, 'book_name': bk.book_name,
                'start_date': start_date, 'due_date': due_date}
        data.append(item)
    return jsonify(data)


# 流式请求千帆大模型
def get_access_token(ak, sk):
    auth_url = "https://aip.baidubce.com/oauth/2.0/token"
    resp = requests.get(auth_url, params={"grant_type": "client_credentials", "client_id": ak, 'client_secret': sk})
    return resp.json().get("access_token")


def get_stream_response(msg):
    ak = "q9m5F3giOQoz3PB9qAqWsnTx"
    sk = "24t2R0cqGiDpisCBzxzwkL9XxZS8hi8u"
    # 大模型接口URL
    base_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"
    url = base_url + "?access_token=" + get_access_token(ak, sk)
    data = {
        "messages": msg,
        "stream": True
    }
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    return requests.post(url, headers=headers, data=payload, stream=True)


def gen_stream(msg):
    response = get_stream_response(msg)
    for chunk in response.iter_lines():
        chunk = chunk.decode("utf8")
        if chunk[:5] == "data:":
            chunk = chunk[5:]
        yield chunk
        time.sleep(0.01)


@app.route("/eb_stream", methods=['POST'])  # 前端调用的path
def eb_stream():
    body = json.loads(request.data.decode("utf8"))
    print(body)
    msg = body.get("msg")
    print(msg)
    return Response(gen_stream(msg), content_type='text/event-stream')


# 读者留言
@app.route("/student/comment", methods=['GET', 'POST'])
@login_required
def comments_student():
    id = current_user.student_id
    comments = Comments.query.all()
    return render_template('student/comments-student.html', name=session.get('name'), id=id, comments=comments)


# 管理员留言
@app.route("/admin/comment", methods=['GET', 'POST'])
@login_required
def comments_admin():
    id = current_user.admin_id
    comments = Comments.query.all()
    return render_template('admin/comments-admin.html', name=session.get('name'), id=id, comments=comments)


@app.route("/student/comment/add", methods=['GET', 'POST'])
def comments_student_add():
    body = json.loads(request.data.decode("utf8"))
    print(body)
    student_id = body.get('id')
    student_name = body.get('name')
    comment_str = body.get("comment")
    today_date = datetime.date.today()
    today_str = today_date.strftime("%Y-%m-%d")
    today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
    comment_date = int(today_stamp) * 1000
    comment = Comments()
    comment.student_id = student_id
    comment.student_name = student_name
    comment.comment = comment_str
    comment.date = comment_date
    comment.status = 0
    db.session.add(comment)
    db.session.commit()

    return jsonify({'code': 200, 'message': "Success"})


@app.route("/admin/comment/solved", methods=['GET', 'POST'])
def comments_admin_solved():
    body = json.loads(request.data.decode("utf8"))
    print(body)
    comment_id = body.get("comment_id")
    comment = Comments.query.filter_by(id=comment_id).first()
    comment.status = 1
    db.session.add(comment)
    db.session.commit()

    return jsonify({'code': 200, 'message': "Success"})


@app.route("/admin/comment/add", methods=['GET', 'POST'])
def comments_admin_add():
    body = json.loads(request.data.decode("utf8"))
    print(body)
    admin_id = body.get("admin_id")
    comment_id = body.get("comment_id")
    comment_str = body.get("comment")
    today_date = datetime.date.today()
    today_str = today_date.strftime("%Y-%m-%d")
    today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
    comment_date = int(today_stamp) * 1000
    commentAdmin = CommentsAdmin()
    commentAdmin.comment_id = comment_id
    commentAdmin.admin_id = admin_id
    commentAdmin.comment = comment_str
    commentAdmin.date = comment_date
    db.session.add(commentAdmin)
    db.session.commit()

    return jsonify({'code': 200, 'message': "Success"})


@app.route("/admin/comment/get", methods=['GET', 'POST'])
def comments_admin_get():
    body = json.loads(request.data.decode("utf8"))
    print(body)
    comment_id = body.get('id')
    commentsAdmin = CommentsAdmin.query.filter_by(comment_id=comment_id).all()
    comments_list = [comment.to_dict() for comment in commentsAdmin]  # 使用列表推导式转换列表中的每个对象
    return jsonify({"comments": comments_list})


@app.route("/student/announcement", methods=['GET', 'POST'])
def announcement_student():
    announcements = Announcements.query.all()
    return render_template('student/announcements-student.html', name=session.get('name'), announcements=announcements)


@app.route("/admin/announcement", methods=['GET', 'POST'])
@login_required
def announcement_admin():
    announcements = Announcements.query.all()
    return render_template('admin/announcements-admin.html', name=session.get('name'), id=session.get('id'),
                           announcements=announcements)


@app.route("/announcement/<id>", methods=['GET', 'POST'])
def announcement_browse(id):
    name = current_user.name if session.get('name') is None else session.get('name')
    announcements = Announcements.query.filter_by(id=id).first()
    with open(f'static/announcements/{id}.md', 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    return render_template('announcement_browse.html', name=name, title=announcements.name, markdown_text=markdown_text)


@app.route("/admin/announcement_add", methods=['GET', 'POST'])
def announcement_admin_add():
    form = AnnouncementForm()
    return render_template('admin/post_announcement.html', name=session.get('name'), form=form)


@app.route("/admin/announcement_post", methods=['GET', 'POST'])
def post_announcement():
    if request.method == 'POST':
        title = request.form.get('title')
        file_text = request.form['file_text']
        print(file_text)
        print(type(file_text))

        if title and file_text:
            # 创建announcement实例并设置标题和日期
            announcement = Announcements()
            announcement.name = title
            today_date = datetime.date.today()
            today_str = today_date.strftime("%Y-%m-%d")
            today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
            comment_date = int(today_stamp) * 1000
            announcement.date = comment_date

            # 添加到数据库会话并提交以获取ID
            db.session.add(announcement)
            db.session.commit()

            # 重命名文件并保存到本地
            filename = f"{announcement.id}.md"
            file_path = os.path.join('static/announcements', filename)
            with open(file_path, 'w', encoding='utf-8') as file:
                # 将字符串写入文件
                file.write(file_text)

            return jsonify({'code': 200, 'message': "Success", 'id': announcement.id})

    return jsonify({'code': 500, 'message': "Failure"})


if __name__ == '__main__':
    app.run()
