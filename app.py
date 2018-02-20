from flask import Flask, request, render_template
from flask_security.forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import IntegerField, StringField, TextAreaField

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jigar@localhost/OnStoreSystem'
db = SQLAlchemy(app)


class ExtendedRegisterForm(RegisterForm):
    mobile_no = IntegerField('Mobile No.')
    pin_number = IntegerField('Pin number')
    address = TextAreaField()
    city = StringField('City')
    pincode = IntegerField('Pin code')

    def __init__(self, form):
        self.mobile_no = form['mobile']
        self.pin_number = form['pinNo']
        self.address = form['address']
        self.city = form['city']
        self.pincode = form['pincode']


@app.route('/login')
@app.route('/login/')
def login_render():
    return render_template('login.html')


@app.route('/register')
@app.route('/register/', methods=['GET', 'POST'])
def register_render():
    if request.method == 'POST':
        import pdb
        pdb.set_trace()
        return render_template('signup.html')
    else:
        return render_template('signup.html')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
