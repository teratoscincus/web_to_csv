"""Create and configure the app."""

from flask import Flask

from web_to_csv.views import view


def create_app():
    """Factory function returning the configured Flask app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile("config.py")

    # View paths
    app.register_blueprint(view)

    return app
