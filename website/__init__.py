import os
from flask import Flask, request, session, render_template, redirect, url_for


def create_app():
    app = Flask(__name__)

    from website.views.main_view import main_view
    app.register_blueprint(main_view, url_prefix='/')

    return app
