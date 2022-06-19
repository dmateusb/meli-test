from enum import Enum

class StatusCode(Enum):

    OK : int = 200
    INTERNAL_SERVER_ERROR : int = 500
    NOT_FOUND : int = 404
