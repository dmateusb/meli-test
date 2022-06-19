from flask import request
from enums.StatusCode import StatusCode
from helpers.http_handler import HttpHandler
from helpers.math_calculator import MathCalculator
from helpers.rebel_satellite import RebelSatellite
from interfaces.finder import Finder


class TopSecret:

    def __init__(self, falcon_finder) -> None:

        self.__falcon_finder: Finder = falcon_finder(RebelSatellite, 
                        MathCalculator(), HttpHandler())
        self.__data_handler = HttpHandler()

    def post(self):

        satellites_data = self.__data_handler.get_json_param('satellites')
        res = self.__falcon_finder.find(satellites_data)
        return self.__data_handler.handle_response(res, StatusCode.OK.value)
