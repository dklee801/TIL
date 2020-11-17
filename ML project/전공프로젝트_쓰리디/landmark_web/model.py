from flask import Flask, render_template, request
import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import load_model
import requests
import pickle

model = load_model('static/landmark_densenet201_270by480_9918.h5', compile=False)

def read_image(image_path):
    image = tf.io.read_file(image_path)
    return tf.image.decode_jpeg(image, channels=3)

def image_pipeline(img, img_size):
    img = tf.cast(img, tf.float32)
    img = tf.dtypes.cast(img, tf.float32)
    img = img / 255
    result_img = tf.image.resize(img, img_size)

    return result_img

def pred_image(image_path):
    # checkpoint_path = "training_1/cp.ckpt"
    # checkpoint_dir = os.path.dirname(checkpoint_path)
    # latest = tf.train.latest_checkpoint(checkpoint_dir)
    # print(latest)
    # model.load_weights(latest)
    
    image = read_image(image_path)
    image = image_pipeline(image, (270, 480))
    image = tf.reshape(image, (1,270,480,3))


    print('start pred')
    pred = model.predict(image)
    probs_argsort = tf.argsort(pred, direction='DESCENDING')
    print(probs_argsort[:5])

    category = pd.read_csv('category.csv')
        
    probs = []
    classes = []
    for i in range(5):
        probs.append(pred[0][[probs_argsort[0][i]]])
        idx = probs_argsort[0][i]
        classes.append(category['landmark_name'][category['landmark_id'] == idx].values[0])

    probs = list(map(lambda x: f'{round(x,3) * 100}%', probs))

    return classes, probs

def google_map(search_name): # 해당 맛집 위도, 경도 불러오는 함수
    URL = f'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDvZ1AOTaBUt4DqGBPm8EEY6NUXonDrwbs&sensor=false&language=ko&address={search_name}'
    response = requests.get(URL)
    data = response.json()
    print(data)
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    return lat, lng


