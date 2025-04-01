from flask import Flask, request, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__, template_folder="../frontend") # Tell Flask where to look

# Load trained model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    email_text = ""

    if request.method == "POST":
        email_text = request.form["email_text"]
        transformed_text = vectorizer.transform([email_text]) # Transform input text
        prediction = model.predict(transformed_text)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
    
    return render_template("index.html", result=result, email_text=email_text)

if __name__ == "__main__":
    app.run(debug=True)