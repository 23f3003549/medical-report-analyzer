from flask import Flask 

def create_app():
    app = Flask(__name__)

    app.config["UPLOAD_FOLDER"] = "uploads"

    from app.routes.upload_routes import upload_bp
    app.register_blueprint(upload_bp)

    return app