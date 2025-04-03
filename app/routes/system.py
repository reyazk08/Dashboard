from flask import Blueprint, render_template

system_bp = Blueprint('system', __name__)

@system_bp.route('/system')
def system_management():
    return render_template('system.html')