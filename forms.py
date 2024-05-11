from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class Login(FlaskForm):
    account = StringField(u'账号', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登录')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'原密码', validators=[DataRequired()])
    password = PasswordField(u'新密码', validators=[DataRequired(), EqualTo('password2', message=u'两次密码必须一致！')])
    password2 = PasswordField(u'确认新密码', validators=[DataRequired()])
    submit = SubmitField(u'确认修改')


class EditInfoFormAdmin(FlaskForm):
    name = StringField(u'用户名', validators=[Length(1, 32)])
    submit = SubmitField(u'提交')


class EditInfoFormStudent(FlaskForm):
    name = StringField(u'用户名', validators=[Length(1,32)])
    sex = StringField(u'性别',validators=[Length(2)])
    telephone = StringField(u'电话号码', validators=[Length(11)])
    submit = SubmitField(u'提交')


class SearchBookForm(FlaskForm):
    methods = [('book_name', '书名'), ('author', '作者'), ('class_name', '类别'), ('isbn', 'ISBN')]
    method = SelectField(choices=methods, validators=[DataRequired()], coerce=str)
    content = StringField()
    submit = SubmitField('搜索')


class SearchStudentForm(FlaskForm):
    card = StringField(validators=[DataRequired()])
    submit = SubmitField('搜索')


class StoreForm(FlaskForm):
    barcode = StringField(validators=[DataRequired(), Length(6)])
    isbn = StringField(validators=[DataRequired(), Length(13)])
    location = StringField(validators=[DataRequired(), Length(1, 32)])
    num= StringField(validators=[DataRequired(),Length(1,3)])
    submit = SubmitField(u'提交')


class WriteOffForm(FlaskForm):
    barcode = StringField(validators=[DataRequired(), Length(6)])
    isbn = StringField(validators=[DataRequired(), Length(13)])
    submit = SubmitField(u'确认')    


class NewStoreForm(FlaskForm):
    isbn = StringField(validators=[DataRequired(), Length(13)])
    book_name = StringField(validators=[DataRequired(), Length(1, 64)])
    press = StringField(validators=[DataRequired(), Length(1, 32)])
    author = StringField(validators=[DataRequired(), Length(1, 64)])
    class_name = StringField(validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField(u'提交')


class BorrowForm(FlaskForm):
    card = StringField(validators=[DataRequired()])
    book_name = StringField()
    submit = SubmitField(u'搜索')
