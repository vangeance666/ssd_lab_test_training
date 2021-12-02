import os
from flask import Flask, request, session, render_template, redirect, url_for



from flask_wtf.csrf import CSRFProtect, CSRFError

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'the random string' 
    csrf.init_app(app)
    from website.views.main_view import main_view
    app.register_blueprint(main_view, url_prefix='/')

    return app
