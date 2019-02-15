from dct import dct2, idct2
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/image', methods=["POST"])
def image():
    sourceImage = request.files["sourceImage"].read()
    #file = request.files['sourceImage']
    #print(file)
    return 'Hello, World!'

app.run()