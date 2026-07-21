from flask import Flask

from routes import main_bp 


def create_app() -> Flask:
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)

    app.register_blueprint(main_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)