from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html', title="Home")

# About Us Page
@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        return redirect(url_for('home'))
    return render_template('login.html', title="Login")

if __name__ == 'main':
    app.run(debug=True)