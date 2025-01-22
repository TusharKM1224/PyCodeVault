import keras
import pickle as pickle
from keras.utils import pad_sequences
import numpy as np

model=keras.models.load_model('sentiment_analysis_model.h5')
with open('tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)


def sentiment_ana(text_input):
    text_sequence = tokenizer.texts_to_sequences([text_input])
    padded_text_sequence=pad_sequences(text_sequence,maxlen=100)
    predicted_rating=model.predict(padded_text_sequence)[0]
    if np.argmax(predicted_rating)==0:
        print(np.argmax(predicted_rating))
        print( 'Negative')

    elif np.argmax(predicted_rating)!=1:
        print(np.argmax(predicted_rating))
        print("Positive")
    else:
        print(np.argmax(predicted_rating))
        print("Neutral")

#text1 =" shit !   " #negative
#text2 ="I hate the product will not buy this product "#negative
#text3 =" hey i have a pen  " # neutral


text4=" The food served here is pathetic"


sentiment_ana(text4)
