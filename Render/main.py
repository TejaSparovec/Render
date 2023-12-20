from flask import Flask, render_template

app = Flask(__name__) #kreiramo nov objekt po modelu. Flask objekt smo dali v app. 

@app.route("/") #kotroler
def index():
    return render_template("index.html") #povežemo html dokument in kontroler oz handler (python)

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(port="5001", use_reloader=True)