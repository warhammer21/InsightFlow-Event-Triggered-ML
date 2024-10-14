from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
with open('model/churn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Welcome to the Churn Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Expect JSON data in the form of {"data": [...]}
    data = request.get_json(force=True)
    features = np.array(data['data']).reshape(1, -1)

    # Predict churn probability
    prediction = model.predict(features)
    churn_prob = model.predict_proba(features)[0][1]

    # Respond with prediction and churn probability
    return jsonify({
        'churn_prediction': int(prediction[0]),
        'churn_probability': churn_prob
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
