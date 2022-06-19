import pickle
import os

from fastapi import File

class FileManager:

    def __init__(self,
            name = "fuego_de_quazar/collections/satellites.pkl"
        ) -> None:
        self.__name = name

    def save(self, data):
        os.makedirs(os.path.dirname(self.__name), exist_ok=True)
        with open(self.__name, 'wb') as f:
            pickle.dump(data, f)

    def load(self):
        try:
            with open(self.__name, 'rb') as f:
                return pickle.load(f)
        except:
            return []
