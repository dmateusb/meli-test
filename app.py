from flask import Flask
app = Flask(__name__)

import fuego_de_quazar.views

if __name__ == "__main__":
    app.run(debug=True)