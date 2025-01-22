from flask import Flask,jsonify,request
import keras
import pickle as pickle
from keras.utils import pad_sequences
import numpy as np

app=Flask(__name__)

model=keras.models.load_model('sentiment_analysis_model.h5')
with open('tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)

@app.route("/")
def index():
    return "hello"
@app.route("/feedback_mod",methods=['POST'])
def sentiment_ana():
    text_input=request.form.get("msg")
    text_sequence = tokenizer.texts_to_sequences([text_input])
    padded_text_sequence=pad_sequences(text_sequence,maxlen=100)
    predicted_rating=model.predict(padded_text_sequence)[0]
    result={"predict":str(np.argmax(predicted_rating))}
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)
   