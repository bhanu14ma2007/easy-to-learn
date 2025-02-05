from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Flask-Login configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User database (for simplicity, using a dictionary here)
# Dummy user data for login
users = {
    "admin": {"password": "admin123"}
}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)
    return None

# Path for storing uploaded files
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route
@app.route('/')
@login_required
def index():
    books = [
        {'title': 'The Great Maratha', 'author': 'Ranjit Desai', 'image': 'images/ashwattham.jpeg', 'pdf': 'SHIVJI.pdf'},
        {'title': 'Wings of Fire', 'author': 'A.P.J. Abdul Kalam', 'image': 'images/download.jpeg', 'pdf': 'Life Journey on Abdul Kalam.pdf'},
        {'title': 'Ram', 'author': 'Amish Tripathi', 'image': 'images/RAM.jpeg', 'pdf': 'ram.pdf'},
    ]
    return render_template('index.html', books=books)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

# Route to view a PDF
@app.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    # Log user activity
    with open("access_log.txt", "a") as log:
        log.write(f"User '{current_user.id}' accessed file: {filename}\n")
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# File upload route
@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return redirect(url_for('index'))
    return 'Invalid file format', 400

# Run server
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
