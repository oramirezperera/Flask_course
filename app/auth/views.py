from flask import render_template, session, url_for, flash, redirect
from app.forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
         'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('successfully added the user')

        return redirect(url_for('index'))

    return render_template('login.html', **context)