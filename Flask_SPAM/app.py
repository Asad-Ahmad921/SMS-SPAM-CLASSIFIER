from flask import Flask, render_template, request
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer   #  correct import

# Download NLTK resources (one time)
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

ps = PorterStemmer()

def text_processing(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load vectorizer & model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_sms = request.form.get('message')

    if not input_sms:
        return render_template('index.html', prediction_text="Kuch toh likho!")

    transformed_sms = text_processing(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    prediction = "SPAM" if result == 1 else "NOT SPAM"

    return render_template(
        'index.html',
        prediction_text=prediction,
        original_text=input_sms
    )

if __name__ == '__main__':
    app.run(debug=True)
