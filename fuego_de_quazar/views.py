from fuego_de_quazar.controllers.top_secret import TopSecret
from fuego_de_quazar.controllers.top_secret_split import TopSecretSplit
from flask import Flask
from fuego_de_quazar.helpers.millenium_falcon_finder import MilleniumFalconFinder
from app import app

@app.route("/topsecret", methods = ["POST"])
def top_secret_post():
    
    top_secret_controller = TopSecret(MilleniumFalconFinder)
    return top_secret_controller.post()

@app.route("/topsecret_split/<satellite_name>", methods = ["POST"])
def topsecret_split_post(satellite_name):
    
    top_secret_controller = TopSecretSplit(MilleniumFalconFinder)
    return top_secret_controller.post(satellite_name)

@app.route("/topsecret_split", methods = ["GET"])
def topsecret_split_get():
    
    top_secret_controller = TopSecretSplit(MilleniumFalconFinder)
    return top_secret_controller.get()