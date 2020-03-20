from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField, DateField
from wtforms import BooleanField, SubmitField, SelectField, RadioField, FileField
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
petugas = [
    ("", "Tidak Ada"),
    ("koordinator", "Koordinator"),
    ("keamanan", "Keamanan"),
    ("pemantauan", "Pemantauan"),
    ("operasi", "Operasi"),
    ("pemeliharaan", "Pemeliharaan")
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
    jam = SelectField("Jam", choices=jam, validators=[DataRequired()], default=jam[0][0])
    tma = DecimalField('TMA')
    volume = DecimalField('Volume')
    submit = SubmitField('Tambah')


class AddVnotch(FlaskForm):
    sampling = DateField("Hari", default=datetime.datetime.today())
    vn1_tma = DecimalField('Vnotch 1 TMA')
    vn1_deb = DecimalField('Vnotch 1 Debit')
    vn2_tma = DecimalField('Vnotch 2 TMA')
    vn2_deb = DecimalField('Vnotch 2 Debit')
    vn3_tma = DecimalField('Vnotch 3 TMA')
    vn3_deb = DecimalField('Vnotch 3 Debit')
    submit = SubmitField('Tambah')


class AddPiezo(FlaskForm):
    sampling = DateField("Hari", default=datetime.datetime.today())
    p1a = DecimalField('Piezo 1A')
    p1b = DecimalField('Piezo 1B')
    p1c = DecimalField('Piezo 1C')
    p2a = DecimalField('Piezo 2A')
    p2b = DecimalField('Piezo 2B')
    p2c = DecimalField('Piezo 2C')
    p3a = DecimalField('Piezo 3A')
    p3b = DecimalField('Piezo 3B')
    p3c = DecimalField('Piezo 3C')
    p4a = DecimalField('Piezo 4A')
    p4b = DecimalField('Piezo 4B')
    p4c = DecimalField('Piezo 4C')
    p5a = DecimalField('Piezo 5A')
    p5b = DecimalField('Piezo 5B')
    p5c = DecimalField('Piezo 5C')
    submit = SubmitField('Tambah')


class AddKegiatan(FlaskForm):
    sampling = DateField("Hari", default=datetime.datetime.today())
    foto = FileField("Foto")
    petugas = SelectField("Petugas", choices=petugas, validators=[DataRequired()], default=petugas[0][0])
    uraian = StringField('Keterangan', validators=[DataRequired()])
    submit = SubmitField('Tambah')
