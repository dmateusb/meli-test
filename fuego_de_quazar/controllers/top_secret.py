from fuego_de_quazar.enums.StatusCode import StatusCode
from fuego_de_quazar.helpers.millenium_falcon_finder import MilleniumFalconFinder
from fuego_de_quazar.helpers.http_handler import HttpHandler
from fuego_de_quazar.helpers.math_calculator import MathCalculator


class TopSecret:

    def __init__(self) -> None:
        self.__math_calculator = MathCalculator()
        self.__data_handler = HttpHandler()
        self.__falcon_finder = MilleniumFalconFinder(
            self.__math_calculator, self.__data_handler)

    def post(self):

        satellites_data = self.__data_handler.get_json_param('satellites')
        res = self.__falcon_finder.find(satellites_data)
        return self.__data_handler.handle_response(res, StatusCode.OK.value)
