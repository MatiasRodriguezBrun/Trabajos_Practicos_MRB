from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__) #intanciar el objeto "app"
prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 38},
    {"id": 2, "tipo": "pantalon", "talle": 48}
    ]

@app.get("/") #home/inicio
def home():
    return render_template("home.html")

@app.get("/prendas/")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"

@app.get("/prendas/<id>") #asume que le podemos pasar cualquier id
def get_prendas(id):
        return f"<p>Mostrando la prenda {escape(id)}</p>"

