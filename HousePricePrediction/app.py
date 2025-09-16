from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("model/house_model.pkl", "rb") as f:
    model = pickle.load(f)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        sqft = float(data['sqft'])
        bedrooms = int(data['bedrooms'])
        bathrooms = int(data['bathrooms'])

        features = np.array([[sqft, bedrooms, bathrooms]])
        prediction = model.predict(features)[0]

        return jsonify({'prediction': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

