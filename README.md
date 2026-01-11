# Student Performance Prediction System (Machine Learning + Flask)

## 📌 Project Overview
This project is an end-to-end machine learning application that predicts a student’s academic performance based on study habits and lifestyle factors.  
A supervised machine learning model is trained using Python and deployed through a Flask web application to provide real-time predictions via a user-friendly interface.

This project demonstrates practical skills in Python programming, data preprocessing, machine learning, and basic web deployment, developed to strengthen my profile for undergraduate Computer Science programs.

---

## 🎯 Problem Statement
Academic performance depends on multiple factors beyond intelligence alone, such as study hours, attendance, sleep patterns, and screen time.  
The goal of this project is to build a data-driven system that predicts whether a student is likely to perform well academically using these measurable factors.

---

## 📊 Dataset
The dataset contains synthetically generated but realistic student data with the following features:

- Study hours per day  
- Attendance percentage  
- Sleep hours per day  
- Daily screen time  
- Previous exam score  

**Target Variable:**
- `1` → Good academic performance  
- `0` → Poor academic performance  

The dataset is balanced and expanded to improve model reliability and reduce prediction errors.

---

## 🧠 Machine Learning Approach
- Type: Supervised Learning (Classification)
- Algorithm: Logistic Regression
- Evaluation Metric: Accuracy

The model is trained using a train–test split and saved for later inference in the web application.

---

## 🌐 Web Application
The trained model is integrated into a Flask web application where users can:
1. Enter academic and lifestyle details
2. Submit the form
3. Receive an instant prediction on academic performance

This demonstrates the deployment of a machine learning model in a real-world, user-facing system.

---

## 🛠️ Technologies & Tools Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask  
- HTML (Jinja2 templates)  

---

## 📂 Project Structure

student-performance-prediction-flask-ml/
│
├── data/
│   └── student_data.csv
│
├── model/
│   └── trained_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── main.py          # trains & saves model
├── app.py           # Flask web app (MAIN WEB FILE)
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Train the machine learning model
python main.py

### 3️⃣ Run the Flask web application
python app.py

### 4️⃣ Open in browser
Navigate to:
http://127.0.0.1:5000
(or open Port 5000 in GitHub Codespaces)

---


## 📈 Results
- The model achieves stable accuracy due to an expanded and balanced dataset
- Study hours, attendance, and previous scores show strong influence on predictions
- Real-time predictions are successfully generated via the web interface

---


