from abc import ABC, abstractclassmethod
from typing import Tuple, List, Text


class Finder(ABC):

    @abstractclassmethod
    def get_location(self, distance: float) -> Tuple[float, float]:
        pass
    
    @abstractclassmethod
    def get_message(self, message : List[Text]) -> Text:
        pass