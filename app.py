from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import User, UserInteraction

app = Flask(__name__, template_folder="templates", static_folder="templates\static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kwamina.db'
db = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template('intro.html')

@app.route('/submit_username', methods=['POST'])
def submit_username():
    username = request.form['name']
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)