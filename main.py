import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import joblib

def load_data(file_path):
    """Load data from a CSV file"""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Preprocess the dataset"""
    X, y = data.iloc[:, :-1].values, data.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test), y_train, y_test

def train_model(X_train, y_train):
    """Train the AI model"""
    param_grid = {'hidden_layer_sizes': [(50,), (100,), (150,)], 'max_iter': [300, 500, 700], 'alpha': [0.0001, 0.001, 0.01]}
    model = GridSearchCV(MLPClassifier(random_state=42), param_grid, cv=3, n_jobs=-1).fit(X_train, y_train)
    print(f"Best parameters: {model.best_params_}")
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the AI model"""
    y_pred = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n')
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

def save_model(model, file_path):
    """Save the trained model"""
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")

def visualize_data(data):
    """Visualize the dataset"""
    pd.plotting.scatter_matrix(data, alpha=0.2, figsize=(10, 10))
    plt.show()

if __name__ == "__main__":
    # Load guinea pig dataset
    data = load_data('guinea_pig_dataset.csv')
    visualize_data(data)
    X_train, X_test, y_train, y_test = preprocess_data(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, 'guinea_pig_trained_model.pkl')
    print("Guinea pig AI model creation completed.")
