from flask import Flask, render_template
from flask_mail import Mail
app = Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'e8350258b9a19a'
app.config['MAIL_PASSWORD'] = '5dfc23fd627920'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/proyect')
def proyect():
    return render_template("portafolio.html")
    
@app.route('/mail_mail')
def send_mail():
    return render_template('send_mail.html')
if __name__ == '__main__':
    app.run(debug=True)