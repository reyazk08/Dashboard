from flask import Blueprint, render_template
from app.services.data_analysis import get_historical_data

historical_bp = Blueprint('historical', __name__)

@historical_bp.route('/historical')
def historical():
    data = get_historical_data()
    return render_template('historical.html', data=data)