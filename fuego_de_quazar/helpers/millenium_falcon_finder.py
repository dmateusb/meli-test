from cmath import exp
from typing import List, Text, Tuple, Dict
from fuego_de_quazar.enums.StatusCode import StatusCode
from fuego_de_quazar.interfaces.finder import Finder

class MilleniumFalconFinder(Finder):

    def get_location(self, distances: List[float]) -> Tuple[float, float]:

        rebel1 = self.__satellites[0]
        rebel2 = self.__satellites[1]

        self.rebel12_distance = self.__calculator.calculate_distance(
            rebel1.get_coordinates(), 
            rebel2.get_coordinates()
        )

        return self.__calculate_position(distances)

    def get_message(self, messages: List[List[Text]]) -> Text:

        self.__satellites[0].set_message(messages[0])
        self.__satellites[1].set_message(messages[1])
        self.__satellites[2].set_message(messages[2])

        return self.__sync_messages()


    def find(self, satellites_data: List[Dict]) -> Dict:

        self.__satellites_data = satellites_data
        distances = self.__extract_distances()
        messages = self.__extract_messages()

        try:
            points = self.get_location(distances)
            message = self.get_message(messages)

        except (ValueError, Exception) as error:
            return self.__data_handler.handle_response(
                str(error), StatusCode.INTERNAL_SERVER_ERROR.value
            )    

        return self.__generate_response(points, message)

    def handle_data(self, satellite_name: Text) -> None:

        distance = self.__data_handler.get_json_param('distance')
        message = self.__data_handler.get_json_param('message')
        satellite = self.__get_satellite(satellite_name)
        satellite.set_falcon_distance(distance)
        satellite.set_message(message)
        self.__file_manager.save(self.__satellites)

    def split_find(self) -> Dict:

        if self.__check_satellites_status():
            distances = [ satellite.get_falcon_distance() for satellite in self.__satellites ]
            messages = [ satellite.get_message() for satellite in self.__satellites ]
            
            try:
                points = self.get_location(distances)
                message = self.get_message(messages)
            
            except (ValueError, Exception) as error:
                return self.__data_handler.handle_response(
                    str(error), StatusCode.INTERNAL_SERVER_ERROR.value
                )    
                

            self.__file_manager.save(None)
            return self.__generate_response(points, message)

    def __extract_distances(self):
        return self.__get_satellite_field(self.__satellites_data, 'distance')
        

    def __extract_messages(self):
        return self.__get_satellite_field(self.__satellites_data, 'message')

    def __check_satellites_status(self):

        for satellite in self.__satellites:
            if not bool(satellite.get_message()):
                return False
        
        return True

    def __get_satellite(self, name):

        func = lambda x: x.get_name() == name 
        return list( filter(func, self.__satellites) )[0]
        
    def __sync_messages(self):

        messages = list(map(lambda x: x.get_message(), self.__satellites))
        final_message = []
        
        for i in range(len(messages[0])):
            j = 0

            while messages[j][i] == '' and j + 1 < len(messages):
                j += 1

            if messages[j][i] == '':
                raise Exception("Not enough information.")
            
            final_message.append(messages[j][i])

        return " ".join(final_message)

    def __calculate_position(self, distances: List[float]):

        rebel1 = self.__satellites[0]
        rebel2 = self.__satellites[1]
        rebel3 = self.__satellites[2]
            
        points = self.__calculator.find_point(
            rebel1.get_coordinates(),
            rebel2.get_coordinates(),
            rebel3.get_coordinates(),
            distances[0],
            distances[1],
            distances[2],
            self.rebel12_distance
        )
        return points

    def __get_satellite_field(self, satellites, field):

        return [satellite[field] for satellite in satellites]

    def __get_satellites_list(self):

        if (self.__file_manager) and self.__file_manager.load():
            return self.__file_manager.load()

        rebel1 = self.__rebel_satellite("kenobi", (-500, -200))
        rebel2 = self.__rebel_satellite("skywalker", (100, -100))
        rebel3 = self.__rebel_satellite("sato", (500, 100))

        return [rebel1, rebel2, rebel3]

    def __generate_response(self, points, message):

        return {
            'position' : {
                'x': points[0],
                'y': points[1]
            },
            'message': message
        }

    def __init__(
        self,
        rebel_satellite,
        calculator,
        data_handler,
        file_manager=None) -> None:

        self.__rebel_satellite = rebel_satellite
        self.__calculator = calculator
        self.__data_handler = data_handler
        self.__file_manager = file_manager
        self.__satellites = self.__get_satellites_list()
