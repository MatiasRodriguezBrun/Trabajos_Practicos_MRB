from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__) 

@app.get("/") 
def home():
    return render_template("home.html")

@app.get("/resultados/") 
def get_resultados():
    return render_template("resultados.html")


# plan_2023

