from flask_bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
moment = Moment(app)
class NameForm(FlaskForm):
 name = StringField('What is your name?', validators=[DataRequired()])
 submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'), current_time=datetime.utcnow())
@app.route('/user/<name>')
def user(name):
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name, current_time=datetime.utcnow())
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

bootstrap = Bootstrap(app)