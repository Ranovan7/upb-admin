from flask import Blueprint
from flask_login import login_required
from app.models import ManualDaily

bp = Blueprint('kinerja', __name__)


@bp.route('')
@login_required
def index():
    pass


@bp.route('/<bendungan_id>')
@login_required
def bendungan(bendungan_id):
    pass


@bp.route('/<bendungan_id>/lapor', methods=['GET', 'POST'])
@login_required
def lapor(bendungan_id):
    pass


@bp.route('/<bendungan_id>/uraian', methods=['GET', 'POST'])
@login_required
def uraian(bendungan_id):
    pass


@bp.route('/<bendungan_id>/tanggapan', methods=['GET', 'POST'])
@login_required
def tanggapan(bendungan_id):
    pass


@bp.route('/<bendungan_id>/update', methods=['GET', 'POST'])
@login_required
def update(bendungan_id):
    pass
