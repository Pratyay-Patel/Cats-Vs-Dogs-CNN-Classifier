import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
MODEL_PATH = "models/cats_dogs_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

UPLOAD_FOLDER = os.path.join("static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def clear_uploads():
    """Delete all files in the uploads folder before saving new ones."""
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    return "Dog" if prediction[0][0] > 0.5 else "Cat"

@app.route("/", methods=["GET", "POST"])
def upload_and_predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            # Clear old uploads before saving new one
            clear_uploads()

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            prediction = predict_image(filepath)

            uploaded_image_url = url_for("static", filename=f"uploads/{filename}")

            return render_template(
                "index.html",
                prediction=prediction,
                uploaded_image=uploaded_image_url
            )

    return render_template("index.html", prediction=None, uploaded_image=None)

if __name__ == "__main__":
    app.run(debug=True)
