from weather import app, db
from flask import render_template, redirect, flash, url_for
from weather.models import WeatherInfo, User
from weather.forms import WeatherForm, RegisterForm, LoginForm
from flask_login import login_user, logout_user, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/weather', methods=['GET', 'POST'])
def weather_page():
    form = WeatherForm()
    if form.validate_on_submit():
        weather_info = WeatherInfo(city=form.city.data)
        return render_template('weather_info.html', weather_info=weather_info)

    return render_template('weather.html', form=form)


@app.route('/weather_in_your_city')
def weather_in_your_city_page():
    if current_user.is_authenticated:
        weather_info = WeatherInfo(city=current_user.city)
        return render_template('weather_info.html', weather_info=weather_info)
    else:
        flash("You need to login before accessing this field", category='danger')
        return redirect(url_for('login_page'))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data,
                              country=form.country.data, city=form.city.data, password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f'You have successfully created your account, now you are logged in as: {user_to_create.username}',
              category='success')
        return redirect(url_for('weather_in_your_city_page'))

    if form.errors != {}:
        for err_mes in form.errors.values():
            flash(err_mes, category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"You have successfully logged in as: {attempted_user.username}", category='success')
            return redirect(url_for('weather_in_your_city_page'))
        else:
            flash('Username and password do not match, please try again.', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash(f"You have been logged out, hope to see you again!", category='success')
    return redirect(url_for('home_page'))

