import unittest
from regex import P
import requests


class TestTopSecret(unittest.TestCase):

    def test_top_secret(self):
        url = "http://127.0.0.1:5000/topsecret"
        headers = {"Content-Type": "application/json"}
        body = get_body()
        res = requests.post(url=url,
            headers=headers,
            json=body,
            verify=False
        )

        self.assertEqual(res.status_code, 200)

def get_body():
    return {
            "satellites": [
                {
                    "name": "kenobi",
                    "distance": 800.0,
                    "message": [
                        "",
                        "",
                        "",
                        "mensaje",
                        ""
                    ]
                },
                {
                    "name": "skywalker",
                    "distance": 400,
                    "message": [
                        "",
                        "es",
                        "",
                        "",
                        "secreto"
                    ]
                },
                {
                    "name": "sato",
                    "distance": 424.51,
                    "message": [
                        "este",
                        "",
                        "un",
                        "",
                        ""
                    ]
                }
            ]
        }

if __name__ == '__main__':
    unittest.main()
