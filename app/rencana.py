from flask import Blueprint
from flask_login import login_required
from app.models import ManualDaily

bp = Blueprint('rtow', __name__)


@bp.route('')
@login_required
def index():
    pass


@bp.route('/<bendungan_id>')
@login_required
def bendungan(bendungan_id):
    pass


@bp.route('/<bendungan_id>/export')
@login_required
def exports(bendungan_id):
    pass


@bp.route('/<bendungan_id>/import')
@login_required
def imports(bendungan_id):
    pass


@bp.route('/<bendungan_id>/update')
@login_required
def update(bendungan_id):
    pass
