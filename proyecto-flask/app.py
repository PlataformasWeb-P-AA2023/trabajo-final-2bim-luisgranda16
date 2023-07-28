from flask import Flask, render_template
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/personas")
def personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/personas/",
            auth=(usuario, clave))
    personas = json.loads(r.content)['results']
    numero_personas = json.loads(r.content)['count']
    return render_template("personas.html", personas=personas,
    numero_personas=numero_personas)

@app.route("/barrios")
def barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrios/",
            auth=(usuario, clave))
    barrios = json.loads(r.content)['results']
    numero_barrios = json.loads(r.content)['count']
    return render_template("barrios.html", barrios=barrios,
    numero_barrios=numero_barrios)

@app.route("/localesCo")
def localesCo():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/localCo/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("localesCo.html", datos=datos,
    numero=numero)

@app.route("/localesRe")
def localesRe():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/localRe/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("localesRe.html", datos=datos,
    numero=numero)
