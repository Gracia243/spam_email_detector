## Spam Email Detector

__A machine learning project to classify emails as spam or not spam using Python, Flask and Scikit-learn.__

### Dataset Source

## Dataset Source

This project uses the **Email Spam Classification Dataset** from Kaggle, originally compiled from the **2007 TREC Public Spam Corpus**.

- __Dataset Author__: [PuruSinghvi](https://www.kaggle.com/datasets/purusinghvi)
- __Source__: [Kaggle Dataset](https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset)
- **Total Records**: 83,446 emails
- **License**: Refer to Kaggle page for terms of use

All credit goes to the original authors and contributors of the dataset.


### Features
- [x] Train a machine learning model to detect spam emails.
- [x] Web-based UI to classify emails in real-time.
- [x] Uses __Naïve Bayes__ with __TF-IDF vectorization__ for accuracy.
- [x] Flask backend to process user input and return predictions.


### Project structure

```txt
spam_email_detector/
│── backend/
│   ├── app.py               # Flask backend
│   ├── train_model.ipynb    # Jupyter Notebook for training
│   ├── spam_email_dataset.csv  # Training dataset
│   ├── spam_model.pkl       # Trained ML model
│   ├── vectorizer.pkl       # Text vectorizer
│   ├── requirements.txt     # Python dependencies
├── frontend/
│   ├── index.html       # Web UI
│── dataset/
│── README.md                # Project documentation
│── .gitignore               # Files to ignore in GitHub
```

### Installation
#### 1. Clone the Repository

```bash
git clone https://github.com/Gracia243/spam_email_detector.git
cd spam_email_detector/backend
```

### 2. Download the Dataset

Since GitHub does not support large files (over 22MB), you need to **download the dataset manually** from Kaggle.

1. **Go to Kaggle**:  
   👉 [Email Spam Classification Dataset](https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset)

2. **Download `spam_email_dataset.csv`**  

3. **Move the file to the `backend/` folder** so that it can be used for training.  

#### 3. Install Dependencies
Make sure you have Python 3 installed, then run:

```bash
pip install -r requirements.txt
```

#### 4. Train the Model
Open Jupyter Notebook and run the training script:

```bash
jupyter notebook train_model.ipynb
```
This will generate `spam_model.pkl`and `vectorizer.pkl`.

#### 5. Start the Flask App
```bash
python app.py
```
The app will be live at:
`http://127.0.0.1:5000/`


### Usage
1. Open the __web app__ in a browser.
2. Paste an email text into the input box.
3. Click "Check" and see if it's __Spam__ or __Not Spam__!


### Model Performance

- __Algorithm__: Naïve Bayes
- __Dataset__: 83,446 emails from Kaggle
- __Accuracy__: __~97%__ 

### Contributing
Got ideas or improvements? Feel free to fork the repo and submit a PR!

### License
This project is licensed under the __MIT License__ – see the [LICENSE](LICENSE) file for details.
