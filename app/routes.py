from sqlite3 import IntegrityError
from app import app ,db
from flask import render_template,redirect,url_for,flash ,request,get_flashed_messages

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/register",methods=['GET','POST'])
def register_page():
    return render_template("register.html")

@app.route("/login",methods=['GET','POST'])
def login_page():
    return render_template("login.html")

@app.route("/history",methods=["GET"])
def history_page():
    return render_template("history.html")