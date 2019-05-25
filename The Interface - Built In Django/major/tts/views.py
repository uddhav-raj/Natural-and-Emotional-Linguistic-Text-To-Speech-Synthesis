from django.http import HttpResponse
from django.shortcuts import render
import main_code as mc
import emotion as em
import shutil
import pickle
import keras_preprocessing
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


def index(request):
    return render(request, 'tts/index.html')

# Create your views here.
def predict(request):

    text = request.POST.get('sentence')
    actor_str = request.POST.get('actor')
    emotion = em.get_emotion_from_text(text)
    actor = 1

    if actor_str == 'Male':
        actor = 0

    octaves = 0
    rate = 0

    if emotion == 0:
        octaves, rate = mc.get_anger_values(actor)
    elif emotion == 1:
        octaves, rate = mc.get_disgust_values(actor)
    elif emotion == 2:
        octaves, rate = mc.get_fearful_values(actor)
    elif emotion == 3:
        octaves, rate = mc.get_sad_values(actor)
    elif emotion == 4:
        octaves, rate = mc.get_happy_values(actor)
    elif emotion == 5:
        octaves, rate = mc.get_sad_values(actor)
    elif emotion == 6:
        octaves, rate = mc.get_sad_values(actor)
    elif emotion == 7:
        octaves, rate = mc.get_surprised_values(actor)

    filename, r_no = mc.convert_to_neutral_audio(text)

    filename2 = mc.change_actor_of_voice(filename, actor, r_no)
    filename3 = mc.change_pitch(filename2, actor, r_no, octaves)
    filename4 = mc.change_rate(filename3, r_no, rate)
    src = "C:\\Users\\hp\\Desktop\\doit\\major\\" + filename4
    dest = "C:\\Users\\hp\\Desktop\\doit\\major\\tts\\static\\tts\\audio\\" + filename4
    shutil.copy(src, dest)
    label_dict = ['Anger', 'Disgust', 'Fearful', 'Sad', 'Happy', 'Sad', 'Sad', 'Surprised']
    predicted_emotion = label_dict[emotion]

    context = {'text': text, 'predicted_emotion' : predicted_emotion, 'actor': actor_str, 'file': filename4}

    return render(request, 'tts/predict.html', context)