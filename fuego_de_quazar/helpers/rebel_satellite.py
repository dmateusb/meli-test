from typing import List, Text, Tuple


class RebelSatellite():


    def get_coordinates(self):
        return self.__coordinates

    def set_coordinates(self, coordinates):
        self.__coordinates = coordinates

    def get_falcon_distance(self):
        return self.__falcon_distance

    def set_falcon_distance(self, falcon_distance: float):
        self.__falcon_distance = falcon_distance

    def get_name(self):
        return self.__name

    def set_name(self, name: Text):
        self.__name = name

    def get_message(self):
        return self.__message

    def set_message(self, message: List[Text]):
        self.__message = message
    

    def __init__(self, name: Text, coordinates: Tuple[int, int]):
        self.__name = name
        self.__coordinates = coordinates
        self.__falcon_distance = None
        self.__message = None

    def __repr__(self) -> str:
        return self.__name