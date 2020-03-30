from flask import Blueprint, jsonify, request
from app.models import Bendungan


bp = Blueprint('api', __name__)


@bp.route('/bendungan')
def bendungan():
    sampling = request.values.get('sampling')
    bends = Bendungan.query.all()

    result = [bend for bend in bends]

    return jsonify(result)
