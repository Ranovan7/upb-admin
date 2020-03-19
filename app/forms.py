from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField, DateField
from wtforms import BooleanField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired
from app.models import Bendungan
import datetime

bends = [(b.id, b.name) for b in Bendungan.query.all()]
bends.insert(0, (0, "Tidak Ada"))
roles = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
]
jam = [
    ('06', '06'),
    ('12', '12'),
    ('18', '18')
]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Ingat saya')
    submit = SubmitField('Login')


class AddUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    bendungan = SelectField("Bendungan", choices=bends, validators=[DataRequired()], default=bends[0][0], coerce=int)
    role = SelectField("Role", choices=roles, validators=[DataRequired()], default=roles[0][0])
    submit = SubmitField('Tambah')


class AddDaily(FlaskForm):
    sampling = DateField("Hari", default=datetime.datetime.today())
    curahhujan = DecimalField('Curah Hujan')
    inflow_deb = DecimalField('Inflow Debit')
    inflow_vol = DecimalField('Inflow Volume')
    outflow_deb = DecimalField('Outflow Debit')
    outflow_vol = DecimalField('Outflow Volume')
    spillway_deb = DecimalField('Spillway Debit')
    spillway_vol = DecimalField('Spillway Volume')
    submit = SubmitField('Tambah')


class AddTma(FlaskForm):
    hari = DateField("Hari", default=datetime.datetime.today())
    jam = SelectField("Jam", choices=jam, validators=[DataRequired()], default=roles[0][0])
    tma = DecimalField('TMA')
    volume = DecimalField('Volume')
    submit = SubmitField('Tambah')
