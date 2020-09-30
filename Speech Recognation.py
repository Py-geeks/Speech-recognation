import speech_recognition as spr
import pyttsx3

r = spr.Recognizer()

def sayit(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):
    try:
        with spr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2,duration=0.2)

            audio2 = r.listen(source2)

            Mytext = r.recognize_google(audio2)
            Mytext = Mytext.lower()

            print("Did You Say "+Mytext)
            sayit(Mytext)

    except spr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except spr.UnknownValueError:
        print("Unknown Error Occured")