import os
import openai
import urllib.request, json
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from models import db, User, UserInteraction

app = Flask(__name__, template_folder="templates", static_folder="templates\static" )
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kwamina.db'
#db = SQLAlchemy(app)
app.secret_key = os.urandom(24)
basedir = os.path.abspath(os.path.dirname("app.py"))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'kwamina.db')
db.init_app(app)


@app.route('/')   
def home():
    return render_template('intro.html')


@app.route('/submit_username', methods=['POST'])   
def submit_username():
    username = request.form['name']
    user = User(username=username)
    session['user'] = username
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/index')    
def index():
    user = session['user']
    return render_template('index.html', user=user)


@app.route('/index', methods=['GET','POST'])
def get_response():
    message = request.form['message']
    openai.api_key = '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'
    model_engine = "text-davinci-003"
    prompt = message
     # Generate a response
    completion = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
      )

    response = completion.choices[0].text
    print(response)
    success = 1
    
      
    return render_template('index.html', response=response, success=success, message=message)     
      
      
    #if not api_key:
        #return 'Error: API key not found', 500
    #try:
       # url = 'https://api.openai.com/v1/completions'
        #data = {
       #     'engine':"davinci-codex",
       #     'prompt': message,
       #     'max_tokens': 2048,
       #     'temperature': 0.5
       # }
       # headers = {
       #     'Authorization': f'Bearer {openai.api_key}',
       #     'Content-Type': 'application/json'
        #}
        #data = json.dumps(data).encode('utf-8')
        #req = urllib.request.Request(url, data, headers)
        #with urllib.request.urlopen(req) as response:
       #     result = json.loads(response.read().decode('utf-8'))
       # response_text = result['choices'][0]['text']
       # success = 1
    #except (urllib.error.URLError, KeyError) as e:
     #   print(f'Error: {e}')
        #return 'Error: could not complete request', 500
    #


if __name__ == '__main__':
    app.run(debug=True)
