import pickle
import numpy as np
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Load the trained Ridge model
with open("C:/Users/Bhoomika NS/house-price-predictor/ridge_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the scaler
with open("C:/Users/Bhoomika NS/house-price-predictor/scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [float(request.form[key]) for key in request.form.keys()]
        
        # Convert to numpy array and reshape for model
        features_array = np.array(features).reshape(1, -1)
        
        # Scale the input
        scaled_features = scaler.transform(features_array)
        
        # Predict house price
        prediction = model.predict(scaled_features)[0]

        return render_template("result.html", prediction=round(prediction, 2))

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
