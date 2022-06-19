import re
from typing import Tuple
from fuego_de_quazar.helpers.http_handler import HttpHandler
import math


class MathCalculator:

    @staticmethod
    def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]):

        x = abs(point1[0] - point2[0])
        y = abs(point1[1] - point2[1])
        return math.sqrt(x ** 2 + y ** 2)

    @staticmethod
    def find_point(point1, point2, point3, ratio1, ratio2, ratio3,
                p1_p2_distance):

        p1 = point1
        p2 = point2
        p3 = point3
        p1_p2_d = p1_p2_distance

        if (p1_p2_d > ratio1 + ratio2) or (p1_p2_d < abs(ratio1 - ratio2)):
            raise ValueError('There are no solutions')

        if (ratio1 == ratio2 and p1 == p2):
            raise ValueError('Can not find the right solution')

        a = ((ratio1 ** 2) - (ratio2 ** 2) +
             (p1_p2_d ** 2)) / (2 * p1_p2_d)
            
        h = math.sqrt((ratio1 ** 2) - (a ** 2))

        p2x = p1[0] + a * ((p2[0] -
                            p1[0]) / p1_p2_d)

        p2y = p1[1] + a * ((p2[1] -
                            p1[1]) / p1_p2_d)

        x0_right_part = h * ((p2[1] - p1[1])
                            / p1_p2_d)

        y0_right_part = h * ((p2[0] - p1[0])
                            / p1_p2_d)

        x0 = p2x + x0_right_part
        y0 = p2y - y0_right_part

        if not ((x0 - p3[0]) ** 2 +
                (y0 - p3[1]) ** 2) == (ratio3 ** 2):

            x0 = p2x - x0_right_part
            y0 = p2y + y0_right_part
            return (x0, y0)

        elif ((x0 - p3[0]) ** 2 +
              (y0 - p3[1]) ** 2) == (ratio3 ** 2):
            
            return (x0, y0)

        else:
            raise ValueError('Can not find the right solution')