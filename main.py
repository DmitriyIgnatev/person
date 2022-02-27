import flask
from flask import Flask, render_template
from second_game import LoginForm
from data import db_session
from data.registr import Reg
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# name = "db/blogs.db"
@app.route('/')
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = LoginForm()
    if form.validate_on_submit():
        print('+')
        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        user = Reg()
        user.login = form.login.data
        user.password = form.password.data
        user.duble_password = form.duble_password.data
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.speciality = form.speciality.data
        user.position = form.position.data
        user.address = form.address.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        print(12)
        return flask.redirect('/pas')
    return render_template('login.html', form=form, title='регистрация')

@app.route('/pas')
def pas():
    return render_template('pas.html')





if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


