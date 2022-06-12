import math
from sys import set_coroutine_origin_tracking_depth
from typing import Tuple
from flask import Flask, request
from helpers.millenium_falcon_finder import MilleniumFalconFinder
from helpers.rebel_satellite import RebelSatellite

app = Flask(__name__)


def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]):
    
    x = abs( point1[0] - point2[0] )
    y = abs( point1[1] - point2[1] )
    return math.sqrt( x ** 2 + y ** 2 )


@app.route("/topsecret", methods = ["POST"])
def hello_world():

    rebel1 = RebelSatellite("Kenobi", (-500, -200))
    rebel2 = RebelSatellite("Skywalker", (100, -100))
    rebel3 = RebelSatellite("Sato", (500, 100))
    satellites = [rebel1, rebel2, rebel3]

    rebel12_dinstance = calculate_distance(rebel1.get_coordinates(), rebel2.get_coordinates())
    rebel13_dinstance = calculate_distance(rebel1.get_coordinates(), rebel3.get_coordinates())    
    rebel23_dinstance = calculate_distance(rebel2.get_coordinates(), rebel3.get_coordinates())    

    falcon_finder = MilleniumFalconFinder(satellites)
    falcon_finder.add_distance(rebel1, rebel2, rebel12_dinstance)
    falcon_finder.add_distance(rebel1, rebel3, rebel13_dinstance)
    falcon_finder.add_distance(rebel2, rebel3, rebel23_dinstance)
    
    satellites_body_data = request.get_json()['satellites']
    falcon_finder.set_request_data(satellites_body_data)
    falcon_finder.calculate_position()