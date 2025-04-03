from flask import Flask

app = Flask(__name__)

from app.routes import dashboard, historical, control, system

app.register_blueprint(dashboard.bp)
app.register_blueprint(historical.bp)
app.register_blueprint(control.bp)
app.register_blueprint(system.bp)