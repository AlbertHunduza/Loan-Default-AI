from flask import Flask, render_template, request
import torch
from models import LoanBinaryModel  # Imports the model class
import numpy as np

app = Flask(__name__)

# Load the saved state_dict into the model
input_dim = 34  # number of input features in the dataset
hidden_dim = 16  # hidden dimension in the model that gave the best results
model = LoanBinaryModel(input_dim, hidden_dim)
model.load_state_dict(torch.load("models/loan_binary_model_state_dict.pth"))
model.eval()

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        features = []  # Collect features from the form
        # Populate 'features' list with form data

        # Convert the list of features to a PyTorch tensor
        features_tensor = torch.tensor(features, dtype=torch.float32).view(1, -1)

        # Make a prediction using the model
        with torch.no_grad():
            prediction = model(features_tensor)
        
        # Convert prediction to a binary label
        label = "Safe" if prediction >= 0.5 else "Risky"
        
        result = f"The loan is predicted to be {label}."
        
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)