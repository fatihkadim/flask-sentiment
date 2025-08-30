from sqlite3 import IntegrityError
from app import app ,db
from flask import render_template,redirect,url_for,flash ,request,get_flashed_messages
from app.models import User ,InputText, SentimentResult
from app.forms import LoginForm, RegisterForm
from flask_login import current_user,login_user,login_required
from nlp.model import analyze_sentiment
from nlp.preprocessing import clean_text
from nlp.utils import format_result


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/sentiment", methods=['GET','POST'])
def sentiment_page():
    if request.method == "POST":
        user_input = request.form.get('text')
        if user_input:
            processed_text = clean_text(user_input)
            sentiment = analyze_sentiment(processed_text)
            result = format_result(sentiment)
            return render_template('sentiment.html', result=sentiment)

    return render_template("sentiment.html")


@app.route("/register",methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_add = User(username=form.username.data,email_address =form.email_address.data,password=form.password1.data)
        db.session.add(user_to_add)
        try:
            db.session.commit()
            login_user(user_to_add)
            flash(message="User created successfuly.",category="success")
            return redirect(url_for(''))

        except IntegrityError:
            db.session.rollback()
            flash(message="This email is already registered. Please try another email.", category="danger")

        return redirect(url_for('sentiment_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(message=f'There was an error with creating a user: {err_msg}',category="danger")

    return render_template("register.html")

@app.route("/login",methods=['GET','POST'])
def login_page():
    return render_template("login.html")

@app.route("/history",methods=["GET"])
def history_page():
    return render_template("history.html")