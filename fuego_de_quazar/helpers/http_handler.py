from flask import make_response, request
from typing import Text


class HttpHandler:

    def get_json_param(self, param: Text):
        return request.get_json()[param]


    def handle_response(self, message: Text, code: int):
        return make_response(
            message,
            code
        )
