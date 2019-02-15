from dct import dct2, idct2
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io 
import numpy as np
import base64

app = Flask(__name__)
CORS(app)

def serve_pil_image(pil_img):
    img_io = io.BytesIO()
    print()
    img_io.seek(0)
    return send_file(img_io, mimetype='image/bmp')

# Dunno, not sure we actually need to base64 the buffer/PIL image
# We still need to serialize it to wrap it in JSON, someway

def pil_to_base64(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, format='bmp')
    return base64.b64encode(img_io.getvalue())

@app.route('/image', methods=["POST"])
def image():
    bytestream = request.files["sourceImage"].read()
    img = Image.open(io.BytesIO(bytestream))
    imagearray = np.asarray( img, dtype="float" )
    print(imagearray.shape)
    h = imagearray.shape[0]
    w = imagearray.shape[1]
    print(dct2(imagearray))

    # DO THINGS ON THE IMAGE
    img = Image.fromarray(idct2(dct2(imagearray)).astype(np.uint8), mode='L')

    # Back to UTF8, which is JSON safe, we will base64 it again on the frontend..
    return jsonify(image="data:image/bmp;base64,"+pil_to_base64(img).decode('utf8'))

app.run()