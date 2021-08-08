from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='log in')


app = Flask(__name__)
app.secret_key = "Morganions have a Big Onions"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST", "GET"])
def receive_data():
    form = LoginForm()
    form.validate_on_submit()
    if form.validate_on_submit() and form.email.data == "admin@email.com" and form.password.data == "12345678":
        return render_template("success.html")
    elif form.validate_on_submit():
        return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
