# main.py
import numpy as np  # Importing numpy for numerical operations
import pandas as pd  # Importing pandas for data manipulation
from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting data
from sklearn.preprocessing import StandardScaler  # Importing StandardScaler for scaling features
from sklearn.neural_network import MLPClassifier  # Importing MLPClassifier for neural network model
from sklearn.metrics import accuracy_score  # Importing accuracy_score for model evaluation

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
    # Initializing the neural network model with one hidden layer
    model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
    
    # Training the model
    model.fit(X_train, y_train)
    
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """Function to evaluate the AI model"""
    y_pred = model.predict(X_test)  # Predicting the target variable for test set
    
    # Calculating the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f'Accuracy: {accuracy * 100:.2f}%')

# Main function
if __name__ == "__main__":
    # Load the dataset
    data = load_data('path_to_dataset.csv')  # Specify the path to your dataset
    
    # Preprocess the data
    X_train, X_test, y_train, y_test = preprocess_data(data)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    print("AI model creation process completed.")
