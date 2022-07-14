from fuego_de_quazar.controllers.top_secret import TopSecret
from fuego_de_quazar.controllers.top_secret_split import TopSecretSplit
from flask import Blueprint

topsecret_page = Blueprint('topsecret', __name__)

@topsecret_page.route("/topsecret", methods = ["POST"])
def top_secret_post():
    
    top_secret_controller = TopSecret()
    return top_secret_controller.post()

@topsecret_page.route("/topsecret_split/<satellite_name>", methods = ["POST"])
def topsecret_split_post(satellite_name):
    
    top_secret_controller = TopSecretSplit()
    return top_secret_controller.post(satellite_name)

@topsecret_page.route("/topsecret_split", methods = ["GET"])
def topsecret_split_get():
    
    top_secret_controller = TopSecretSplit()
    return top_secret_controller.get()
