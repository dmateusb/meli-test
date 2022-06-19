from abc import ABC, abstractclassmethod
from typing import Tuple, List, Text, Dict


class Finder(ABC):

    @abstractclassmethod
    def get_location(self, distance: float) -> Tuple[float, float]:
        pass
    
    @abstractclassmethod
    def get_message(self, message : List[Text]) -> Text:
        pass

    @abstractclassmethod
    def find(self, satellites_data: List[Dict]) -> Dict:
        pass

    @abstractclassmethod
    def handle_data(self, satellite_name: Text) -> None:
        pass

    @abstractclassmethod
    def split_find(self) -> Dict:
        pass
