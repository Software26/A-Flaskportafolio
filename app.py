from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/proyect')
def proyect():
    return render_template("portafolio.html")
    
    
if __name__ == '__main__':
    app.run(debug=True)