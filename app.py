from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Database ka path set kar rahe hain
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Table ka model banate hain
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    users = User.query.all()  # Saare users fetch karo
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
    return render_template('greet.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Pehli baar run hone par database create karega
    app.run(debug=True)
