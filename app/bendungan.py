from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from app.models import Bendungan
from app.models import ManualDaily, ManualTma, ManualVnotch, ManualPiezo, Rencana
from app import db
from sqlalchemy import and_, desc, cast, Date
from pprint import pprint
from pytz import timezone
import datetime

bp = Blueprint('bendungan', __name__)


@bp.route('/')
@login_required
def index():
    ''' Home Bendungan '''
    waduk = Bendungan.query.all()
    date = request.values.get('sampling')
    def_date = datetime.datetime.utcnow()
    sampling = datetime.datetime.strptime(date, "%Y-%m-%d") if date else def_date
    end = sampling + datetime.timedelta(days=1)

    data = []
    for w in waduk:
        daily = ManualDaily.query.filter(
                                    and_(
                                        ManualDaily.sampling >= sampling,
                                        ManualDaily.sampling <= end),
                                    ManualDaily.bendungan_id == w.id
                                    ).first()
        vnotch = ManualVnotch.query.filter(
                                    and_(
                                        ManualVnotch.sampling >= sampling,
                                        ManualVnotch.sampling <= end),
                                    ManualVnotch.bendungan_id == w.id
                                    ).first()
        tma = ManualTma.query.filter(
                                    and_(
                                        ManualTma.sampling >= sampling,
                                        ManualTma.sampling <= end),
                                    ManualTma.bendungan_id == w.id
                                    ).all()
        # if daily:
        #     print(daily.sampling)
        # if tma:
        #     print(tma[0].sampling)
        tma_d = {
            '6': None,
            '12': None,
            '18': None,
        }
        for t in tma:
            tma_d[f"{t.sampling.hour}"] = None if not t.tma else round(t.tma/100, 1)

        data.append({
            'id': w.id,
            'nama': w.nama,
            'volume': w.volume,
            'lbi': w.lbi,
            'elev_puncak': w.elev_puncak,
            'muka_air_max': w.muka_air_max,
            'muka_air_min': w.muka_air_min,
            'tma6': tma_d['6'],
            'tma12': tma_d['12'],
            'tma18': tma_d['18'],
            'outflow_vol': None if not daily else daily.outflow_vol,
            'outflow_deb': None if not daily else daily.outflow_deb,
            'spillway_deb': None if not daily else daily.spillway_deb,
            'curahhujan': None if not daily else daily.ch,
            'debit': None if not vnotch else vnotch.vn_deb
        })

    return render_template('bendungan/index.html',
                            waduk=data,
                            sampling=sampling)


@bp.route('/<bendungan_id>', methods=['GET'])
@login_required
def bendungan(bendungan_id):
    bend = Bendungan.query.get(bendungan_id)
    return render_template('bendungan/bendungan.html',
                            bend=bend)


@bp.route('/<bendungan_id>/update', methods=['POST'])
@login_required
def update(bendungan_id):
    bend = Bendungan.query.get(bendungan_id)
    attr = request.values.get('name')
    val = request.values.get('value')
    setattr(bend, attr, val)
    db.session.commit()

    result = {
        "name": attr,
        "pk": bendungan_id,
        "value": val
    }
    return jsonify(result)
