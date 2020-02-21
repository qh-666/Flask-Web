from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user
from passlib.handlers.sha2_crypt import sha256_crypt

from website.form import RegistrationForm
from website import app,db
from website.User import User

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    registerform=RegistrationForm(request.form)
    if request.method == 'POST' and registerform.validate():
        email=registerform.email.data
        username=registerform.username.data
        password=sha256_crypt.hash(str(registerform.password.data))
        #into db
        new_user=User(email=email,username=username,password=password)
        db.session.add(new_user)
        try:
            db.session.commit()
            print('-----already into database-----')
            flash('You are now registered successfully and can log in', 'success')
            return redirect(url_for('login'))
            #redirect(url_for('home'))
        except :
            db.session.rollback()
            print('-----rollback-----')
    return render_template('register.html',form=registerform)