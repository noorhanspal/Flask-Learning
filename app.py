from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        username = request.form.get('username')
        color = request.form.get('color')
        new_user = User(username=username, color=color)
        db.session.add(new_user)
        db.session.commit()
        return f"Saved! Hello, {username}! Your favorite color is {color} 🌈"
    return render_template('greet.html')  # ← Yaha par function end hota hai

# 👇 Yaha update route sahi jagah par likho (function ke bahar)
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.color = request.form.get('color')
        db.session.commit()
        return "User updated successfully!"
    return render_template('update.html', user=user)

@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return "User deleted successfully!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
