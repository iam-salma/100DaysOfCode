from flask import Flask, render_template
from flask_bootstrap import Bootstrap5 # pip install bootstrap-flask
from myform import MyForm

'''
On Windows type:
python -m pip install -r requirements.txt
'''

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "mysecretkey"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "salmasyed1360@gmail.com" and form.password.data == "123456789":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
