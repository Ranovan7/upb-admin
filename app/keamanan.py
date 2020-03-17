from flask import Blueprint
from flask_login import login_required
from app.models import ManualDaily

bp = Blueprint('keamanan', __name__)


@bp.route('')
@login_required
def index():
    pass


@bp.route('/<bendungan_id>')
@login_required
def bendungan(bendungan_id):
    pass


@bp.route('/<bendungan_id>/vnotch', methods=['GET', 'POST'])
@login_required
def vnotch(bendungan_id):
    pass


@bp.route('/<bendungan_id>/vnotch/update', methods=['GET', 'POST'])
@login_required
def vnotch_update(bendungan_id):
    pass


@bp.route('/<bendungan_id>/piezo', methods=['GET', 'POST'])
@login_required
def piezo(bendungan_id):
    pass


@bp.route('/<bendungan_id>/piezo/update', methods=['GET', 'POST'])
@login_required
def piezo_update(bendungan_id):
    pass
