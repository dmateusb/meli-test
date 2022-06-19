from fuego_de_quazar.enums.StatusCode import StatusCode
from flask import request
from fuego_de_quazar.helpers.http_handler import HttpHandler
from fuego_de_quazar.helpers.millenium_falcon_finder import MilleniumFalconFinder
from fuego_de_quazar.helpers.math_calculator import MathCalculator
from fuego_de_quazar.helpers.file_manager import FileManager


class TopSecretSplit:

    def __init__(self) -> None:
        self.__data_handler = HttpHandler()
        self.__math_calculator = MathCalculator()
        self.__file_manager = FileManager()
        self.__falcon_finder = MilleniumFalconFinder(self.__math_calculator,
            self.__data_handler, self.__file_manager)

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
