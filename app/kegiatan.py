from flask import Blueprint, request, redirect, url_for, jsonify
from flask_login import login_required
from app.models import Kegiatan
from app import db

bp = Blueprint('kegiatan', __name__)


@bp.route('/')
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


@bp.route('/update', methods=['POST'])
@login_required
def update():
    pk = request.values.get('pk')
    attr = request.values.get('name')
    val = request.values.get('value')
    row = Kegiatan.query.get(pk)
    setattr(row, attr, val)
    db.session.commit()

    result = {
        "name": attr,
        "pk": pk,
        "value": val
    }
    return jsonify(result)
