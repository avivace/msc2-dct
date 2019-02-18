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
import time

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
    totalTime = time.process_time()
    bytestream = request.files["sourceImage"].read()
    
    preTime = time.process_time()

    beta = float(request.form["beta"])
    img = Image.open(io.BytesIO(bytestream))

    if (beta!=1):

        d = int(request.form["d"])
        f = np.asarray(img, dtype="float")

        preTime = time.process_time() - preTime

        dct2Time = time.process_time()
        c = dct2(f)
        dct2Time = time.process_time() - dct2Time

        betaTime = time.process_time()
        apply_beta_transform(d, beta, c)
        betaTime = time.process_time() - betaTime

        idct2Time = time.process_time()
        ff = idct2(c).astype(np.uint8)
        idct2Time = time.process_time() - idct2Time

        normTime = time.process_time()
        norm(ff)
        normTime = time.process_time() - normTime

        img = Image.fromarray(ff, mode='L')
        totalTime = time.process_time() - totalTime
    else:
        preTime=0;
        dct2Time=0;
        idct2Time=0;
        betaTime=0;
        normTime=0;
        totalTime=0;
    # Back to UTF8, which is JSON safe, we will base64 it again on the frontend..
    return jsonify(image="data:image/bmp;base64,"+pil_to_base64(img).decode('utf8'),
        preTime=round(preTime,3),
        dct2Time=round(dct2Time,3),
        idct2Time=round(idct2Time,3),
        betaTime=round(betaTime,3),
        normTime=round(normTime,3),
        totalTime=round(totalTime,3))

app.run()