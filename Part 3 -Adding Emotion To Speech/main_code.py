import os
import subprocess
import shutil


def convert_to_neutral_audio(text):
    from gtts import gTTS
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    import random
    r_no = random.randint(1,1000)
    filename = "inp" + str(r_no) + ".mp4"
    myobj.save(filename)
    return filename, r_no

def change_actor_of_voice(filename, actor, r_no):
    if actor==0:
        var = 'ffmpeg -i C:\\Users\\hp\\Desktop\\doit\\'+ filename + ' -af asetrate=24000*3/4,atempo=4/3 out1'+ str(r_no) +'.mp4'
        v = subprocess.call(var, shell=True)
    else:
        src = filename
        dest = "out1"+ str(r_no) +".mp4"
        shutil.copy(src, dest)
    changed_filename = 'out1'+ str(r_no) +'.mp4'
    return changed_filename



def change_pitch(filename, actor, r_no, octaves):
    from pydub import AudioSegment
    from pydub.playback import play

    
    sound = AudioSegment.from_file(filename)
    new_sample_rate = int(sound.frame_rate * octaves)
    changed_pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    changed_pitch_sound = changed_pitch_sound.set_frame_rate(changed_pitch_sound.frame_rate)
    exported_filename = "out2"+ str(r_no) +".mp4"
    changed_pitch_sound.export(exported_filename, format="mp4")
    return exported_filename

        
def change_rate(filename, r_no, rate):
    exported_filename = "out3"+ str(r_no) +".wav"
    var = 'ffmpeg -i ' + filename + ' -af atempo='+ str(rate) +" "+ exported_filename
    v = subprocess.call(var, shell=True)
    return exported_filename

def get_anger_values(actor):
    rate = 1.25
    octaves = 0
    if actor==0:
        octaves=0.8
    else:
        octaves = 1.3
    return octaves, rate

def get_happy_values(actor):
    rate = 0.9
    octaves = 0
    if actor==0:
        octaves = 1.0
    else:
        octaves = 1.1
    return octaves, rate

def get_sad_values(actor):
    rate = 0.7
    octaves = 0
    if actor==0:
        octaves = 0.9
    else:
        octaves = 1
    return octaves, rate

def get_fearful_values(actor):
    rate = 1.1
    octaves = 0
    if actor==0:
        octaves = 0.9
    else:
        octaves = 1.1
    return octaves, rate

def get_neutral_values(actor):
    rate = 1
    octaves = 1
    return octaves, rate

def get_disgust_values(actor):
    rate = 0.75
    octaves = 0
    if actor==0:
        octaves = 0.9
    else:
        octaves = 1.1
    return octaves, rate

def get_surprised_values(actor):
    rate = 1.15
    octaves = 0
    if actor==0:
        octaves = 0.95
    else:
        octaves = 1.1
    return octaves, rate

def get_calm_values(actor):
    rate = 0.75
    octaves = 0
    if actor==0:
        octaves = 1
    else:
        octaves = 1.1
    return octaves, rate
    
text = "Kids are talking by the door"
emotion = 0
actor = 0
# 0 is male 1 is female

octaves, rate = get_happy_values(actor)    
filename, r_no =  convert_to_neutral_audio(text)

filename2 = change_actor_of_voice(filename, actor, r_no)
#filename3 = change_pitch(filename2, actor, r_no, octaves)
#filename4 = change_rate(filename3, r_no, rate)
#os.system(filename4)


