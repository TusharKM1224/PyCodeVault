import numpy as np
import pandas as pd
import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding,Conv1D,GlobalMaxPool1D,Dense,Dropout
import pickle as pickle

df=pd.read_csv('Reddit_Data.csv')
df =df[['clean_comment','category']]
df['clean_comment']=df['clean_comment'].convert_dtypes(str)
df=df[['clean_comment','category']]
df=df.dropna()
print(df['clean_comment'])



df['sentiment']=df['category'].apply(lambda x:'positive' if x > 0 else 'negative' if x<0 else 'Neutral' if x == 'NA' else '')



df= df.sample(frac=1).reset_index(drop=True)
tokenizer=Tokenizer(num_words=5000, oov_token= '')
tokenizer.fit_on_texts(df['clean_comment'])
word_index=tokenizer.word_index
sequences=tokenizer.texts_to_sequences(df['clean_comment'])
padded_sequences = pad_sequences(sequences, maxlen=100, truncating='post')
sentiment_labels=pd.get_dummies(df['sentiment']).values

x_train,x_test,y_train,y_test = train_test_split(padded_sequences,sentiment_labels,test_size=0.2)




model = Sequential()
model.add(Embedding(12000,100,input_length=100))
model.add(Conv1D(64,5,activation='softmax'))
model.add(GlobalMaxPool1D())
model.add(Dense(32,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3,activation='sigmoid'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))
y_pred = np.argmax(model.predict(x_test), axis=-1)
print(" Accuracy : ", accuracy_score(np.argmax(y_test, axis=-1), y_pred.view()))

model.save('sentiment_analysis_model2.h5')
with open('tokenizer.pickle','wb') as handle:
    pickle.dump(tokenizer,handle,protocol=pickle.HIGHEST_PROTOCOL)





#-------------------------------------------------------------------------





