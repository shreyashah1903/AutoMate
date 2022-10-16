import pickle
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer

# Please see Email Classifier for our full model!
MODEL_FILENAME = 'model/finalized_model.sav'
VECTORIZER_FILENAME = 'model/finalized_vectorizer.sav'
ENCODER_FILENAME = 'model/finalized_encoder.sav'
rejection_model = pickle.load(open(MODEL_FILENAME, 'rb'))
vectorizer = pickle.load(open(VECTORIZER_FILENAME, 'rb'))
encoder = pickle.load(open(ENCODER_FILENAME, 'rb'))

category_names = {'reject':'Rejected','not_reject':'Not Rejected'}



def transform_text(body):
    stop_words = set(stopwords.words('english'))
    body = body.lower()
    body = body.translate(str.maketrans('','', string.punctuation))
    body = body.translate(str.maketrans('','','1234567890'))
    body = body.translate(str.maketrans('','','\n'))
    body = ' '.join(word.lower() for word in body.split() if word not in stop_words)
    return body

def predict_rejection(email):
    x = vectorizer.transform([email])
    prediction = rejection_model.predict(x)
    return category_names[encoder.inverse_transform(prediction)[0]]




def uses_job_keywords(words):
    job_reserved_keywords = {'job','offer','recruiter','recruit','applying','recruiting','position','talent','resume','role','selected'}
    for word in words:
        if word in job_reserved_keywords:
            return True
    return False

nltk.download('stopwords')
x = 'Congratulations you have been selected for this position!'
