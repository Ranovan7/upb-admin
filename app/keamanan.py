from flask import Blueprint, request, redirect, url_for, jsonify
from flask_login import login_required
from app.models import ManualVnotch, ManualPiezo
from app import db

bp = Blueprint('keamanan', __name__)


@bp.route('/')
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


@bp.route('/vnotch/update', methods=['POST'])
@login_required
def vnotch_update():
    pk = request.values.get('pk')
    attr = request.values.get('name')
    val = request.values.get('value')
    row = ManualVnotch.query.get(pk)
    setattr(row, attr, val)
    db.session.commit()

    result = {
        "name": attr,
        "pk": pk,
        "value": val
    }
    return jsonify(result)


@bp.route('/<bendungan_id>/piezo', methods=['GET', 'POST'])
@login_required
def piezo(bendungan_id):
    pass


@bp.route('/piezo/update', methods=['POST'])
@login_required
def piezo_update():
    pk = request.values.get('pk')
    attr = request.values.get('name')
    val = request.values.get('value')
    row = ManualPiezo.query.get(pk)
    setattr(row, attr, val)
    db.session.commit()

    result = {
        "name": attr,
        "pk": pk,
        "value": val
    }
    return jsonify(result)
