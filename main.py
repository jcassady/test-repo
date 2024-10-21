# main.py

import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.preprocessing import StandardScaler  # For scaling features
from sklearn.neural_network import MLPClassifier  # For neural network model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # For model evaluation
import matplotlib.pyplot as plt  # For data visualization
from sklearn.model_selection import GridSearchCV  # For hyperparameter tuning
import joblib  # For saving the model

# Load the dataset
def load_data(file_path):
    """Function to load data from a CSV file"""
    data = pd.read_csv(file_path)
    return data

# Preprocess the data
def preprocess_data(data):
    """Function to preprocess the dataset"""
    # Assuming the last column is the target variable
    X = data.iloc[:, :-1].values  # Features
    y = data.iloc[:, -1].values  # Target variable
    
    # Splitting the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

# Train the model
def train_model(X_train, y_train):
    """Function to train the AI model"""
    # Initializing the neural network model with hyperparameter tuning
    param_grid = {
        'hidden_layer_sizes': [(50,), (100,), (150,)],
        'max_iter': [300, 500, 700],
        'alpha': [0.0001, 0.001, 0.01]
    }
    model = GridSearchCV(MLPClassifier(random_state=42), param_grid, cv=3, n_jobs=-1)
    
    # Training the model
    model.fit(X_train, y_train)
    
    print(f"Best parameters found: {model.best_params_}")
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """Function to evaluate the AI model"""
    y_pred = model.predict(X_test)  # Predicting the target variable for test set
    
    # Calculating the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')
    
    # Additional evaluation metrics
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Visualize the results
def visualize_data(data):
    """Function to visualize the dataset"""
    pd.plotting.scatter_matrix(data, alpha=0.2, figsize=(10, 10))
    plt.show()

# Save the model
def save_model(model, file_path):
    """Function to save the trained model"""
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")

# Main function
if __name__ == "__main__":
    # Load the dataset
    data = load_data('path_to_dataset.csv')  # Specify the path to your dataset
    
    # Visualize the data
    visualize_data(data)
    
    # Preprocess the data
    X_train, X_test, y_train, y_test = preprocess_data(data)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Save the model
    save_model(model, 'trained_model.pkl')
    
    print("AI model creation process completed.")
