import datetime
from urllib.parse import urlparse, urljoin
from flask import render_template, redirect, url_for, flash, request, abort, Blueprint
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import desc
from pytz import timezone

from app import app
from app.models import Users, Rencana, Bendungan, Embung, ManualTma, ManualDaily
from app.forms import LoginForm

bp = Blueprint('', __name__)


@app.route('/')
def index():
    ''' Index UPB '''
    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username/Password')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        # next = request.args.get('next')
        # if not is_safe_url(next):
        #     return abort(400)
        return redirect(url_for('index'))
    return render_template('auth/login.html', title='Login', form=form)
