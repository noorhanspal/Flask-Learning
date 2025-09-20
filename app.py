from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        username = request.form.get('username')  # Form se data lena
        color = request.form.get('color')
        return f"Hello, {username}! Your favourite color is {color} 🎉"
    return render_template('greet.html')  # Form dikhana

if __name__ == '__main__':
    app.run(debug=True)
