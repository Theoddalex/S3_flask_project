from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import boto3
from dotenv import load_dotenv
import os

load_dotenv()
s3 = boto3.client('s3')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('hello', name=name))
    return render_template('home.html')

@app.route('/hello/<name>')
def hello(name):
    user = User.query.filter_by(name=name).first()
    if user:
        bucket_name = 'alexbucket222'
        filename = '200w.gif'
        file_url = f'https://{bucket_name}.s3.amazonaws.com/{filename}'
        return render_template('hello.html', name=name, file_url=file_url)
    return 'User not found', 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=5001)
