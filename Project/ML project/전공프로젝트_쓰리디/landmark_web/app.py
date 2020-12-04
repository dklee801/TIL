from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
import numpy as np
import os
import model

app = Flask(__name__, template_folder='Template')
cors = CORS(app)
Bootstrap(app)
"""
Routes
"""
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':

            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            classes, probs = model.pred_image(image_path)
            lat, lng = model.google_map('금천구청')   # search_name
            print(lat)
            print(lng)
            result = {
                'class_name': classes,
                'probs': probs,
                'image_path': image_path,
                'lat' : lat,
                'lng' : lng,
            }
            return render_template('result.html', result = result, lat=lat, lng=lng)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
