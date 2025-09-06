from app import db,login_manager
from flask import redirect,url_for,flash
from app import bcrypt
from flask_login import UserMixin
from datetime import datetime,timezone


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash(message="You need to log in to access this page.", category="warning")
    return redirect(url_for("login_page"))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # Bir kullanıcının birden fazla InputText'i olabilir
    input_texts = db.relationship('InputText', backref='author', lazy=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    credit = db.Column(db.Integer,default=100)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class InputText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text,nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sentiment_result = db.relationship('SentimentResult', backref='analyzed_text', uselist=False,cascade="all, delete-orphan")

    def sent_assign(self,user,commit=True):
        self.user_id = user.id


class SentimentResult(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    sentiment_score = db.Column(db.Float)
    sentiment_label = db.Column(db.String(20))
    input_text_id = db.Column(db.Integer, db.ForeignKey('input_text.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
