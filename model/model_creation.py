# In your local environment
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

# Generate a simple dummy model for demonstration purposes
X = np.array([[0.1, 0.2], [0.3, 0.6], [0.8, 0.4], [0.5, 0.9]])
y = np.array([0, 1, 1, 0])

model = LogisticRegression()
model.fit(X, y)

# Save the model
with open('churn_model.pkl', 'wb') as file:
    pickle.dump(model, file)
