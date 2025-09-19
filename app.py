from flask import Flask, render_template

app = Flask(__name__)

#home page
@app.route('/')
def home():
    name = 'Noor'
    items = ["Python", "Flask","HTML","CSS"]
    return render_template('home.html',user=name,skills=items)

# about page
@app.route('/about')
def about():
    return "this is about page"

# contact page
@app.route('/contact')
def contact():
    @app.route('/contact')
    def contact():
        return "this is contact page"

if __name__ == '__main__':
    app.run(debug=True)
