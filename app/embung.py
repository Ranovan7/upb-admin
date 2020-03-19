from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from app.models import Embung
from app import db

bp = Blueprint('embung', __name__)


@bp.route('/')
@login_required
def index():
    ''' Home Embung '''
    embung = Embung.query.filter(Embung.is_verified == '1').all()

    embung_a = []
    embung_b = []
    for e in embung:
        if e.jenis == 'a':
            embung_a.append(e)
        elif e.jenis == 'b':
            embung_b.append(e)
    return render_template('embung/index.html',
                            embung_a=embung_a,
                            embung_b=embung_b)


@bp.route('/<embung_id>/update', methods=['POST'])
@login_required
def update(embung_id):
    emb = Embung.query.get(embung_id)
    attr = request.values.get('name')
    val = request.values.get('value')
    setattr(emb, attr, val)
    db.session.commit()

    result = {
        "name": attr,
        "pk": embung_id,
        "value": val
    }
    return jsonify(result)
