import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_and_save_model():
    data = pd.read_csv("data/student_data.csv")

    X = data.drop("final_result", axis =1)
    Y = data["final_result"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter= 1000)
    model.fit(X_train, Y_train)

    accuracy = accuracy_score(Y_test, model.predict(X_test))
    print(f"Model accuracy: {accuracy:.2f}")

    with open("model/trained_model.pkl", "wb") as file:
        pickle.dump(model, file)

    print("✅Model trained and saved successfully!!")

if __name__ == "__main__":
    train_and_save_model()
