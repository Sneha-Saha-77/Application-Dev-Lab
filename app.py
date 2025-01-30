from flask import Flask, request, jsonify, render_template
import pickle
import joblib  # Import joblib for model loading (useful for Scikit-learn models)
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Try loading the model with joblib first, fallback to pickle if needed
def load_model():
    try:
        # If the model was saved using joblib, use joblib to load it
        model = joblib.load("logistic_regression_cat_dog_model.pkl")
    except Exception as e:
        try:
            # If it's a pickle file, fallback to pickle
            with open("logistic_regression_cat_dog_model.pkl", "rb") as model_file:
                model = pickle.load(model_file)
        except Exception as e:
            print(f"Error loading model: {e}")
            raise e
    return model

# Load the pre-trained model
model = load_model()

def preprocess_image(image_path):
    """
    Preprocess the image to match the model's input requirements.
    Modify this function based on how the model was trained.
    """
    image = Image.open(image_path).convert("RGB").resize((128, 128))  # Example: Resize to 224x224
    image = np.array(image) / 255.0  # Normalize pixel values (make sure this matches your model's training)
    image = image.flatten()  # Flatten if needed (for non-CNN models)
    return np.expand_dims(image, axis=0)  # Add batch dimension (needed for Scikit-learn models)

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
        
        # Predict using the loaded model
        prediction = model.predict(processed_image)
        predicted_class = prediction[0]  # Adjust based on your model's output format
        
        return jsonify({"class": int(predicted_class)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
