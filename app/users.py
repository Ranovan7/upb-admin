from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required
from app.models import Users, Bendungan
from app.forms import AddUser
from app import db

bp = Blueprint('users', __name__)


@bp.route('/')
@login_required
def index():
    users = Users.query.all()
    bends = Bendungan.query.all()
    return render_template('users/index.html',
                            users=users,
                            bends=bends)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddUser()
    if form.validate_on_submit():
        username = request.values.get('username')
        password = request.values.get('password')
        bendungan_id = request.values.get('bendungan')
        role = request.values.get('role')

        # check if username is available
        if Users.query.filter_by(username=username).first():
            flash('Username tidak tersedia !', 'danger')
            return render_template('users/tambah.html', form=form)

        # save new user data
        new_user = Users(
            username=username,
            bendungan_id=bendungan_id,
            role=role
        )
        # hash password as md5
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.flush()
        db.session.commit()

        flash('Tambah User berhasil !', 'success')
        return redirect(url_for('users.index'))

    return render_template('users/index.html',
                            form=form)


@bp.route('/password', methods=['GET', 'POST'])
@login_required
def password(user_id):
    user = Users.query.get(user_id)
    if request.method == 'POST':
        password = request.values.get('password')
        user.set_password(password)
        db.session.commit()

        flash('Password berhasil diubah !', 'success')
        return redirect(url_for('users.index'))
    return render_template('users/password.html', user=user)


@bp.route('/delete', methods=['GET', 'POST'])
@login_required
def delete(user_id):
    user = Users.query.get(user_id)
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()

        flash('User dihapus !', 'success')
        return redirect(url_for('users.index'))
    return render_template('users/hapus.html', user=user)
