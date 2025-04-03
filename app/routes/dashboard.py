from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    return render_template('dashboard.html')

@dashboard_bp.route('/historical')
def historical():
    return render_template('historical.html')

@dashboard_bp.route('/control')
def control():
    return render_template('control.html')

@dashboard_bp.route('/system')
def system():
    return render_template('system.html')