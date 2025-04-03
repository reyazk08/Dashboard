from flask import Blueprint, render_template, request, redirect, url_for
from app.services.bot_control import start_bot, stop_bot, get_bot_status

control_bp = Blueprint('control', __name__)

@control_bp.route('/control', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'start':
            start_bot()
        elif action == 'stop':
            stop_bot()
        return redirect(url_for('control.control'))

    bot_status = get_bot_status()
    return render_template('control.html', bot_status=bot_status)