from flask import Blueprint, request, redirect, url_for, jsonify
from flask_login import login_required
from app.models import Kerusakan
from app import db

bp = Blueprint('kinerja', __name__)


@bp.route('/')
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


@bp.route('/update', methods=['POST'])
@login_required
def update():
    pk = request.values.get('pk')
    attr = request.values.get('name')
    val = request.values.get('value')
    row = Kerusakan.query.get(pk)
    setattr(row, attr, val)
    db.session.commit()

    result = {
        "name": attr,
        "pk": pk,
        "value": val
    }
    return jsonify(result)
