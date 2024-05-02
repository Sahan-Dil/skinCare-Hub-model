from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

model = None
interpreter = None
input_index = None
output_index = None

class_names = ['black head',
 'flat wart',
 'haelthy skin',
 'keloid',
 'severe acne',
 'simple acne',
 'white head',
 'wrinkles']

BUCKET_NAME = "skin-care-hub-bucket"

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")


def preprocess_image(img):
    image = np.array(
        Image.open(img).convert("RGB").resize((256, 256)) # image resizing
    )
    return image


def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/skhub.h5",
            "/tmp/skhub.h5",
        )
        model = tf.keras.models.load_model("/tmp/skhub.h5")

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    preprocessed_image = preprocess_image(file)

    img_array = tf.expand_dims(preprocessed_image, 0)
    predictions = model.predict(img_array)

    print("Predictions:",predictions[0])

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    # Set CORS headers
    response = jsonify({"class": predicted_class, "confidence": confidence})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    
    return response
