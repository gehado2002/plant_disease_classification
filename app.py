"""
Plant Disease Classification - Inference App
------------------------------------------------
A simple app (e.g. Streamlit/Flask) for loading a trained model
and classifying plant leaf images as healthy or diseased.

Usage (Streamlit example):
    streamlit run app.py
"""

import os

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

MODEL_PATH = os.path.join("models", "plant_disease_efficientnetb0.keras")
IMG_SIZE = (224, 224)

CLASS_NAMES = [
    # TODO: replace with your actual class labels, e.g.
    # "Apple___Black_rot",
    # "Apple___healthy",
    # "Tomato___Late_blight",
]


def load_trained_model(model_path: str = MODEL_PATH):
    """Load a trained Keras model from disk."""
    return load_model(model_path)


def preprocess_image(img_path: str):
    """Load and preprocess an image for prediction."""
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array


def predict(model, img_path: str):
    """Run prediction on a single image and return the class + confidence."""
    img_array = preprocess_image(img_path)
    preds = model.predict(img_array)
    class_idx = int(np.argmax(preds, axis=1)[0])
    confidence = float(np.max(preds))
    label = CLASS_NAMES[class_idx] if CLASS_NAMES else f"class_{class_idx}"
    return label, confidence


if __name__ == "__main__":
    # Minimal CLI usage example:
    #   python app.py path/to/image.jpg
    import sys

    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_image>")
        sys.exit(1)

    model = load_trained_model()
    label, confidence = predict(model, sys.argv[1])
    print(f"Prediction: {label} (confidence: {confidence:.2%})")
