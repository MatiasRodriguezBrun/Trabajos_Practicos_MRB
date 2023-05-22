from flask import Flask

app = Flask(__name__)
prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 38},
    {"id": 2, "tipo": "pantalon", "talle": 48}
    ]
@app.get("/")
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>" #<p> etiqueta de parrafo

#armar la ruta /prendas que muetsre todos los items de prendas