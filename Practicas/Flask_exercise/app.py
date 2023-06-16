from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__) 

@app.get("/") 
def home():
    return render_template("home.html")

@app.get("/conclusiones/")
def get_conclusiones():
    return render_template("plan_2023.html")

@app.get("/resultados/") 
def get_resultados():
    return render_template("resultados.html")
