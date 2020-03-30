from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from flask_login import login_required
from sqlalchemy import and_
from app.models import Bendungan, Rencana
from app import db
import datetime

bp = Blueprint('rtow', __name__)


@bp.route('/')
@login_required
def index():
    sampling = request.values.get('sampling')
    sampling = datetime.datetime.strptime(sampling, "%Y-%m-%d")
    start = datetime.datetime.strptime(f"{sampling.year -1}-11-01", "%Y-%m-%d")
    end = datetime.datetime.strptime(f"{sampling.year}-10-31", "%Y-%m-%d")

    bends = Bendungan.query.all()
    rencana = Rencana.query.filter(
                            and_(
                                Rencana.sampling >= start,
                                Rencana.sampling <= end)).all()
    rtow = {}
    for bend in bends:
        rtow[bend.id] = {
            "bend": bend
        }
    for ren in rencana:
        if ren.sampling.day in [1, 15]:
            rtow[ren.bendungan_id][ren.sampling.day] = ren

    return render_template('rencana/index.html',
                            sampling=sampling,
                            rtow=rtow)


@bp.route('/<bendungan_id>/export', methods=['GET', 'POST'])
@login_required
def exports(bendungan_id):
    bend = Bendungan.query.get(bendungan_id)

    if request.method == "POST":
        pass

    return render_template('rencana/export.html',
                            bend=bend)


@bp.route('/<bendungan_id>/import')
@login_required
def imports(bendungan_id):
    sampling = datetime.datetime.now()
    start = datetime.datetime.strptime(f"{sampling.year - 2}-11-01", "%Y-%m-%d")
    end = datetime.datetime.strptime(f"{sampling.year - 1}-10-31", "%Y-%m-%d")

    bend = Bendungan.query.get(bendungan_id)
    rencana = Rencana.query.filter(
                            and_(
                                Rencana.sampling >= start,
                                Rencana.sampling <= end),
                            Rencana.bendungan_id == bendungan_id).all()

    return render_template('rencana/export.html',
                            bend=bend)


@bp.route('/update', methods=['POST'])
@login_required
def update():
    pk = request.values.get('pk')
    attr = request.values.get('name')
    val = request.values.get('value')
    row = Rencana.query.get(pk)
    setattr(row, attr, val)
    db.session.commit()

    result = {
        "name": attr,
        "pk": pk,
        "value": val
    }
    return jsonify(result)
