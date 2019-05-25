import pickle
import keras_preprocessing
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

def get_emotion_from_text(text):
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    #with open('lstm_isear_model.h5', 'rb') as handle:
        #model = pickle.load(handle)
    #filename = 'lstm_isear_model.h5'
    
    model = load_model('lstm_isear_model.h5')
    label_dict = ['anger', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
    #label_dict = ['anger', 'disgust', 'fear', 'sadness', 'shame', 'joy', 'guilt']

    test_sentence = [text]
    sequences = tokenizer.texts_to_sequences(test_sentence)
    test_data = pad_sequences(sequences, maxlen=100)


    emo = model.predict(test_data)
    g = emo[0][0]
    index = 0
    for i in range(1,6):
        if emo[0][i] > g:
            g = emo[0][i]
            index = i

    return index

text = ""
emotion = get_emotion_from_text(text)
print(emotion)
