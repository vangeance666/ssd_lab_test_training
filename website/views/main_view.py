from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify, flash
import sys
from website.processing.sanitizer import Sanitizer
from website.forms.search_form import SearchForm


main_view = Blueprint('main_view'
	, __name__
	, template_folder='templates'
	, static_folder='static')

@main_view.route('/')
def index():
	# return render_template('upload.html')	
	return render_template('index.html', form=SupportForm())

@main_view.route("/processSearch/", methods=["POST"])
def process_search():

	form = SearchForm()

	if form.validate_on_submit():
		search_text = form.search_text.data

		if Sanitizer.has_xss(search_text):
			flash("XSS String detected", category='error')
			return render_template("index.html") #Wont redirect just regenerate page to clear
		else: #Sucess then redirect to success with a hyper link to redirect back to index. 
			return redirect(url_for("main_view.search_result"))

	return redirect(url_for("main_view.index"))

	
	if request.method == "POST":
		print(request.form, flush=True)

		if request.form and request.form['search-text']:
			search_text = request.form['search-text']

			if Sanitizer.has_xss(search_text):
				flash("XSS String detected")
				return render_template("index.html") #Wont redirect just regenerate page to clear
			else: #Sucess then redirect to success with a hyper link to redirect back to index. 
				return redirect(url_for("main_view.search_result"))

	return redirect(url_for("main_view.index"))



			# return jsonify({"status": "success"
			# 	, "xss_detected": Sanitizer.has_xss(search_text)}), 200

		
	# return jsonify({"status": "Failed"}), 400



@main_view.route("/searchSuccess/", methods=["GET"])
def search_result():
	return render_template("success.html")


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