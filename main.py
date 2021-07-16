import gc
import json
import torch
import easyocr
import numpy as np
from PIL import Image
from flask import Flask, request, abort, make_response, jsonify

# =====================================================================================================================
app = Flask(__name__)


# =====================================================================================================================

def _get_data(detections):
    data = []
    for detection in detections:
        data.append({
            "bbox": detection[0],
            "prediction": detection[1]
        })
        print(detection)
    return data


@app.route("/", methods=["POST"])
def matching():
    file = request.files["image"]
    image = Image.open(file.stream)
    image = np.array(image)

    data = [
        {
            "bbox": [[0, 361], [185, 361], [185, 458], [0, 458]],
            "prediction": "1",
            "score": 0.036499177460890486
        },
        {
            "bbox": [[271.0866267888802, 353.03481093433084], [607.9278978574579, 410.68651124783946],
                     [583.9133732111197, 507.96518906566916], [248.07210214254215, 450.31348875216054]],
            "prediction": "1",
            "score": 0.059745189889387484
        },
        {
            "bbox": [[619.2917949420224, 412.02282160134695], [883.9981954137139, 497.8007573294617],
                     [849.7082050579776, 588.977178398653], [586.0018045862861, 503.1992426705383]],
            "prediction": "1s",
            "score": 0.03412359773704838
        }
    ]
    return jsonify(data)


if __name__ == '__main__':
    app.run()
