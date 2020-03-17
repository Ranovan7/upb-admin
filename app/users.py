from flask import Blueprint
from flask_login import login_required
from app.models import Users

bp = Blueprint('users', __name__)


@bp.route('')
@login_required
def index():
    pass


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    pass


@bp.route('/password', methods=['GET', 'POST'])
@login_required
def password(user_id):
    pass


@bp.route('/delete', methods=['GET', 'POST'])
@login_required
def delete(user_id):
    pass
