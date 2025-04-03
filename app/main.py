from flask import Flask
from app.routes.dashboard import dashboard_bp
from app.routes.historical import historical_bp
from app.routes.control import control_bp
from app.routes.system import system_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(historical_bp)
    app.register_blueprint(control_bp)
    app.register_blueprint(system_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)