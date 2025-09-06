from sqlite3 import IntegrityError
from app import app ,db
from flask import render_template,redirect,url_for,flash ,request,get_flashed_messages
from app.models import User ,InputText, SentimentResult
from app.forms import LoginForm, RegisterForm
from flask_login import current_user,login_user,login_required,logout_user
from nlp.model import analyze_sentiment
from nlp.preprocessing import clean_text
from nlp.utils import format_result


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/sentiment", methods=['GET','POST'])
@login_required
def sentiment_page():
    if request.method == "POST":
        user_input = request.form.get('text')
        if user_input:
            processed_text = clean_text(user_input)
            sentiment = analyze_sentiment(processed_text)
            result = format_result(sentiment)
            try:
                new_input = InputText(text=processed_text)
                new_input.sent_assign(current_user)

                new_result = SentimentResult(
                    sentiment_score=result['score'],
                    sentiment_label=result['label'],
                    input_text_id=new_input.id
                )
                new_input.sentiment_result = new_result
                db.session.add(new_input)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                flash(message=f"An error occurred: {str(e)}", category="danger")

            return render_template('sentiment.html', result=result)

    return render_template("sentiment.html")


@app.route("/register",methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_add = User(username=form.username.data,email =form.email_address.data,password=form.password1.data)
        db.session.add(user_to_add)
        try:
            db.session.commit()
            login_user(user_to_add)
            flash(message="User created successfuly.",category="success")
            return redirect(url_for('sentiment_page'))

        except IntegrityError:
            db.session.rollback()
            flash(message="This email is already registered. Please try another email.", category="danger")
            return redirect(url_for('register_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(message=f'There was an error with creating a user: {err_msg}',category="danger")

    return render_template("register.html",form = form)

@app.route("/login",methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user_attempted = User.query.filter_by(username=form.username.data).first()
        if user_attempted and user_attempted.check_password_correction(attempted_password = form.password.data):
            login_user(user_attempted)
            flash(message="Successfully logged",category="success")
            return  redirect(url_for("sentiment_page"))

        else:
            flash(message="Username and password dont match. Please try again.",category='danger')
    return render_template("login.html",form = form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash(message='You have been logged out.',category='info')
    return redirect(url_for('home_page'))

@app.route("/dashboard",methods=["GET","POST"])
def dashboard_page():
    user_texts = InputText.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", texts=user_texts)