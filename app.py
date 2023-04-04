import os
from flask import Flask, request, render_template, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from utilities.helpers import get_word, login_required, contains_numbers
import random


app = Flask(__name__)

app.secret_key = os.environ["FLASK_SECRET_KEY"]

# create the extension
db = SQLAlchemy()


# Note that the database connection URI specified here is intended for demonstration purposes only.
# In a production environment, it is recommended to connect to a real database server instead of using a local SQLite database.
# You should replace this URI with the appropriate connection string for your production database.
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{os.path.join(os.getenv('TMPDIR', '/tmp'), 'project.db')}"

# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    hash = db.Column(db.String, nullable=False)

class Words(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    word = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        word_length = request.form.get("word_length", None)
        if word_length:
            random_word = get_word(word_length)[0]
        else:
            random_word = get_word()[0]
            
        return render_template("index.html", word=random_word)
    else:
        return render_template("index.html")

@app.route("/from_list", methods=["POST"])
@login_required
def from_list():
    objects = Words.query.filter_by(user_id=session["user_id"]).all()
    word_list = [item.word for item in objects]
    if word_list:
        return render_template("index.html", word=random.choice(word_list))
    else:
        flash("No saved words on your list!")
        return render_template("index.html")


@app.route("/add", methods=["POST"])
@login_required
def add():
    objects = Words.query.filter_by(user_id=session["user_id"]).all()
    word_list = [item.word for item in objects]
    word = request.form.get("submit").lower()
    flag = contains_numbers(word)
    if flag:
        flash(f"It appears word: `{word}` contains a number! Please retry!")
        return redirect(url_for("wordlist"))
    
    # check if the word is in the DB
    if word not in word_list:
        data = Words(user_id=session["user_id"], word=word)
        db.session.add(data)
        db.session.commit()
        flash(f"Successfully add `{word}` to the database!")
    else:
        flash(f"`{word}` is already in your saved word list")
    return redirect(url_for("wordlist"))


@app.route("/remove", methods=["POST"])
@login_required
def remove():
    word = request.form.get("word")
    data = Words.query.filter(Words.user_id==session["user_id"], Words.word==word).first()
    db.session.delete(data)
    db.session.commit()
    flash(f"Successfully removed `{word}` from the database!")
    return redirect(url_for("wordlist"))

@app.route("/wordlist", methods=["GET"])
@login_required
def wordlist():
    word_list = Words.query.filter_by(user_id=session["user_id"]).all()
    return render_template("wordlist.html", word_list=word_list)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", message="username can not be empty!")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("error.html", message="password can not be empty!")

        # Query database for username
        # Ensure username exists and password is correct
        result = User.query.filter_by(username=request.form.get("username")).first()

        if not result:
            return render_template("error.html", message="username is not existed!")
        elif not check_password_hash(result.hash, request.form.get("password")):
            return render_template("error.html", message="password do not match!")

        # Remember which user has logged in
        session["user_id"] = result.id

        # Redirect user to home page
        flash('Successfully logged in!')
        return redirect("/wordlist")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    # return redirect(url_for("login"))
    flash('Successfully logged out!')
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    result = db.session.query(User).all()
    users = [user.username for user in result]

    if request.method == "POST":
        username = request.form.get("username")
        if username in users:
            return render_template("error.html", message="This username has been registered already!")
        password = request.form.get("password")
        if not username:
            return render_template("error.html", message="username can not be empty!")

        # Ensure password was submitted
        elif not password:
            return render_template("error.html", message="password can not be empty!")
        elif password != request.form.get("confirmation"):
            return render_template("error.html", message="password do not match!")
        user = User(
            username=username,
            hash=generate_password_hash(password),
        )
        db.session.add(user)
        db.session.commit()

        # No need to login in after registration
        result = User.query.filter_by(username=username).first()
        session["user_id"] = result.id
        flash('Successfully registed!')
        return redirect("/")

    return render_template("register.html")


@app.route("/check")
def check_name():
    signup_name = request.args.get("user")
    result = db.session.query(User).all()
    users = [user.username for user in result]
    return "red" if signup_name in users else "green"