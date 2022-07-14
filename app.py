from flask import Flask
from fuego_de_quazar.views import topsecret_page
import os

app = Flask(__name__)
app.register_blueprint(topsecret_page)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0",port=port,debug=True)
