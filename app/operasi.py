from flask import Blueprint
from flask_login import login_required
from app.models import ManualDaily

bp = Blueprint('operasi', __name__)


@bp.route('')
@login_required
def index():
    pass


@bp.route('/harian')
@login_required
def harian():
    pass


@bp.route('/<bendungan_id>')
@login_required
def bendungan(bendungan_id):
    pass


@bp.route('/<bendungan_id>/tma')
@login_required
def tma(bendungan_id):
    pass


@bp.route('/<bendungan_id>/tma/update')
@login_required
def tma_update(bendungan_id):
    pass


@bp.route('/<bendungan_id>/daily')
@login_required
def daily(bendungan_id):
    pass


@bp.route('/<bendungan_id>/daily/update')
@login_required
def daily_update(bendungan_id):
    pass
