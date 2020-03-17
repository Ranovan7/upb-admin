from flask import Blueprint
from flask_login import login_required
from app.models import ManualDaily

bp = Blueprint('kegiatan', __name__)


@bp.route('')
@login_required
def index():
    pass


@bp.route('/<bendungan_id>')
@login_required
def bendungan(bendungan_id):
    pass


@bp.route('/<bendungan_id>/paper')
@login_required
def paper(bendungan_id):
    pass


@bp.route('/<bendungan_id>/add', methods=['GET', 'POST'])
@login_required
def add(bendungan_id):
    pass


@bp.route('/<bendungan_id>/update', methods=['GET', 'POST'])
@login_required
def update(bendungan_id):
    pass
