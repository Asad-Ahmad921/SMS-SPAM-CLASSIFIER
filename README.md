# SMS Spam Detection System 📩

This project is a Machine Learning–based **SMS Spam Detection System** integrated with a **Flask web application**.  
It classifies incoming SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

---

##  Features

- Classifies SMS messages as **Spam / Ham**
- Machine Learning model trained on real SMS data
- Clean and simple Flask web interface
- Fast and accurate predictions
- Easy to run locally

---

##  How It Works

1. User enters an SMS message in the web interface  
2. The message is preprocessed (cleaning, tokenization, vectorization)  
3. A trained ML model predicts whether the message is **Spam** or **Not Spam**  
4. The result is displayed instantly on the web page

---

##  Tech Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **NLP:** TF-IDF / Count Vectorizer  
- **Web Framework:** Flask  
- **Model Storage:** Pickle (.pkl)  
- **Frontend:** HTML, CSS  

---

##  Project Structure
SMS-Spam-Detection/
│
├── ml_model/
│ ├── model.pkl
│ ├── vectorizer.pkl
│ └── training_notebook.ipynb
│
├── flask_app/
│ ├── app.py
│ ├── model.pkl
│ ├── vectorizer.pkl
│ ├── templates/
│ └── static/
│
├── requirements.txt
└── README.md
