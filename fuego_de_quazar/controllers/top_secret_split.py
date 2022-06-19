from fuego_de_quazar.enums.StatusCode import StatusCode
from flask import request
from fuego_de_quazar.helpers.http_handler import HttpHandler
from fuego_de_quazar.helpers.rebel_satellite import RebelSatellite
from fuego_de_quazar.helpers.math_calculator import MathCalculator
from fuego_de_quazar.helpers.file_manager import FileManager
from fuego_de_quazar.interfaces.finder import Finder


class TopSecretSplit:

    def __init__(self, falcon_finder) -> None:

        self.__falcon_finder: Finder = falcon_finder(RebelSatellite,
            MathCalculator(), HttpHandler(), FileManager())
        self.__data_handler = HttpHandler()

    def post(self, satellite_name):
        self.__falcon_finder.handle_data(satellite_name)
        return self.__data_handler.handle_response(
            "Satellite actived",
            StatusCode.OK.value
        )

    def get(self):
        
        res = self.__falcon_finder.split_find()
        
        if not (res):
            return self.__data_handler.handle_response(
                message="Not enough information.",
                code=StatusCode.NOT_FOUND.value
            )

        return self.__data_handler.handle_response(res, StatusCode.OK.value)
