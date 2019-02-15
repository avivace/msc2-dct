from dct import dct2, idct2
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io 
import numpy as np
import base64
from beta import apply_beta_transform, norm

app = Flask(__name__)
CORS(app)

def serve_pil_image(pil_img):
    img_io = io.BytesIO()
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

    d = int(request.form["d"])
    beta = float(request.form["beta"])


    img = Image.open(io.BytesIO(bytestream))
    f = np.asarray(img, dtype="float")

    c = dct2(f)

    apply_beta_transform(d, beta, c)

    ff = idct2(c).astype(np.uint8)
    norm(ff)

    img = Image.fromarray(ff, mode='L')

    # Back to UTF8, which is JSON safe, we will base64 it again on the frontend..
    return jsonify(image="data:image/bmp;base64,"+pil_to_base64(img).decode('utf8'))

app.run()