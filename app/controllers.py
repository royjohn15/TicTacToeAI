from flask import Flask
from flask import render_template, request, redirect
from flask import current_app as app
from datetime import datetime

@app.route("/")
def home():
	return render_template("home.html")