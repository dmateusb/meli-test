import math
from typing import Dict, List, Text, Tuple
from interfaces.finder import Finder
from helpers.rebel_satellite import RebelSatellite

class MilleniumFalconFinder(Finder):

    def calculate_position(self):

        rebel1 = self.satellites[0]
        rebel2 = self.satellites[1]
        rebel3 = self.satellites[2]

        
        falcon_distance1 = rebel1.get_falcon_distance()
        falcon_distance2 = rebel2.get_falcon_distance()
        falcon_distance3 = rebel3.get_falcon_distance()
        rebel12_distance = self.distances[rebel1][rebel2]
        breakpoint()

        a = ( ( falcon_distance1 ** 2 ) - ( falcon_distance2 ** 2 ) + 
            ( rebel12_distance ** 2 ) ) / ( 2 * rebel12_distance )
        h = math.sqrt( ( falcon_distance1 ** 2 ) - ( a ** 2 ) )
        x0_right_part = h * ( ( rebel2.get_coordinates()[1] - rebel1.get_coordinates()[2] )
            / rebel12_distance )
        y0_right_part = h * ( ( rebel2.get_coordinates()[0] - rebel1.get_coordinates()[0] )
            / rebel12_distance )
        x0 = rebel1.get_coordinates()[0] + x0_right_part
        y0 = rebel1.get_coordinates()[1] + y0_right_part
        
        # ( ( ( x0  - rebel3.get_coordinates[0] ) ** 2 + ( y0 - rebel3.get_coordinates[1]) ** 2 ) == math.sqrt( falcon_distance3 ) ):
        if not ( ( ( x0  - rebel3.get_coordinates[0] ) ** 2 + 
            ( y0 - rebel3.get_coordinates[1]) ** 2 ) == math.sqrt( falcon_distance3 ) ):
            print("CAMBIO DE SIGNO")
            x0_right_part = x0_right_part * -1
            y0_right_part = y0_right_part * -1
            x0 = rebel1.get_coordinates()[0] + x0_right_part
            y0 = rebel1.get_coordinates()[1] + y0_right_part

        else:
            print(
                ( ( ( x0  - rebel3.get_coordinates[0] ) ** 2 + 
                ( y0 - rebel3.get_coordinates[1]) ** 2 ) == math.sqrt( falcon_distance3 ) )
            )
            


    def set_request_data(self, satellites_body_data):

        for satellite in satellites_body_data:
            func = lambda x: x.get_name().lower() == satellite['name']
            rebel_satellite_list = list(filter(func, self.satellites))
            rebel_satellite = rebel_satellite_list[0]
            rebel_satellite.set_falcon_distance(satellite['distance'])
            rebel_satellite.set_message(satellite['message'])

    def get_location(self, distance: float) -> Tuple[float, float]:
        pass

    def get_message(self, message : List[Text]) -> Text:
        pass

    def add_distance(self, satellite1, satellite2, distance):
        self.distances[satellite1][satellite2] = distance

    def get_distances(self):
        return self.distances

    def __init_distances(self):
        distances = {}

        for satellite in self.satellites:
            distances[satellite] = {}
        return distances

    def __init__(self, satellites : List[RebelSatellite]) -> None:
        self.satellites = satellites
        self.distances : Dict[Tuple[RebelSatellite, float]] = self.__init_distances()
