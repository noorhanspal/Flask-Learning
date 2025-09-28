from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = 'mysecretkey'

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User model (table structure)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)

# 🏠 Home route - show all users
@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)

# 🎨 Greet route - add new user
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        username = request.form.get('username')
        color = request.form.get('color')

        if not username or not color:
            flash("Please fill in all fields!", "warning")
            return redirect(url_for('greet'))

        new_user = User(username=username, color=color)
        db.session.add(new_user)
        db.session.commit()

        flash(f"User '{username}' added successfully! 🎉", 'success')
        return redirect(url_for('home'))

    return render_template('greet.html')

# ✏️ Update user route
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.color = request.form.get('color')

        db.session.commit()
        flash(f"User '{user.username}' updated successfully! ✨", 'info')
        return redirect(url_for('home'))

    return render_template('update.html', user=user)

# ❌ Delete user route
@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    flash(f"User '{user.username}' deleted successfully! 🗑️", 'danger')
    return redirect(url_for('home'))

# 🚀 Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # create the database if not exists
    app.run(debug=True)
