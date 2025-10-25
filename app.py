
from flask import Flask, render_template, request, redirect, url_for, session, flash
from services import account_service, tour_service, promotion_service, review_service
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Trong production nên dùng biến môi trường

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please login first', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    tours = tour_service.get_all_tours()
    promotions = promotion_service.get_all_promotions()
    return render_template('home.html', tours=tours, promotions=promotions)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if account_service.signup(username, password):
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose another.', 'error')
            
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if account_service.login(username, password):
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

@app.route('/accounts')
@login_required
def accounts():
    users = account_service.get_all_accounts()
    return render_template('accounts.html', users=users)

@app.route('/tours')
def tours():
    tours = tour_service.get_all_tours()
    return render_template('tours.html', tours=tours)

@app.route('/tour/<int:tour_id>')
def tour_detail(tour_id):
    tour = tour_service.get_tour_by_id(tour_id)
    if tour is None:
        flash('Tour not found', 'error')
        return redirect(url_for('tours'))
    reviews = review_service.get_reviews_for_tour(tour_id)
    return render_template('tour_detail.html', tour=tour, reviews=reviews)

@app.route('/promotions')
def promotions():
    promotions = promotion_service.get_all_promotions()
    return render_template('promotions.html', promotions=promotions)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='404 - Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='500 - Internal server error'), 500

if __name__ == '__main__':
    app.run(debug=True)
