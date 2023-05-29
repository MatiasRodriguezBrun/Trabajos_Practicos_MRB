from flask import Flask


app = Flask(__name__)
prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 38},
    {"id": 2, "tipo": "pantalon", "talle": 48}
    ]

@app.get("/")
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>" #<p> etiqueta de parrafo

@app.get("/prendas/")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"

#armar la ruta /prendas que muetsre todos los items de prendas