from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/perfil')
def  home():
    return render_template('perfil.html')

@app.route('/inf')
def  inf():
    return render_template('inf.html')

@app.route('/login')
def  login():
    return render_template('login.html')

@app.route('/ventana')
def  ventana():
    return render_template('ventana.html')

if __name__ == '__main__':
    app.run(debug=True)

    