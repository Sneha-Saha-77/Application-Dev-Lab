from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model  # Import Keras' load_model function
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained CNN model from the .h5 file
def load_cnn_model():
    try:
        model = load_model("cnn_cat_dog_model.h5")  # Load the .h5 model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e
    return model

# Load the CNN model
model = load_cnn_model()

def preprocess_image(image_path):
    """
    Preprocess the image to match the CNN model's input requirements.
    Modify this function based on how the model was trained.
    """
    img = image.load_img(image_path, target_size=(128, 128))  # Resize to the input shape of the model
    img_array = image.img_to_array(img)  # Convert image to numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize pixel values (if this was part of the model's preprocessing)
    return img_array

@app.route("/")
def index():
    """Serve the frontend."""
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Handle image uploads and return predictions."""
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image_file = request.files["image"]
    image_path = os.path.join("uploads", image_file.filename)
    os.makedirs("uploads", exist_ok=True)
    image_file.save(image_path)  # Save the uploaded image

    try:
        # Preprocess the image
        processed_image = preprocess_image(image_path)
        
        # Predict using the loaded CNN model
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=1)[0]  # Get the class with highest probability
        
        return jsonify({"class": int(predicted_class)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
