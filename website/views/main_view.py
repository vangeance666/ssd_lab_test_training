from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify, flash

main_view = Blueprint('main_view'
	, __name__
	, template_folder='templates'
	, static_folder='static')

@main_view.route('/')
def index():
	# return render_template('upload.html')
	return render_template('index.html')

# @main_view.route('/upload/')
# def upload():
#     return render_template('upload.html')

# @main_view.route('/overview/')
# def overview():
#     return render_template('overview.html')

# @main_view.route('/results/')
# def results():
#     return render_template('results.html')

# @main_view.route('/statistics/')
# def statistics():
#     return render_template('statistics.html')

#     