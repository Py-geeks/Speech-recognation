# Speech-recognation
This is a basic speech recognition module in python.

### Pre-Requisites

- Speechrecognition: Library for performing speech recognition, with support for several engines and APIs, online and offline.
- Pyaudio: PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library.
- Pyttsx3: This library is used to convert text to speech.

### Installing Libraries

         pip install speechrecognition
         pip install pyaudio
         pip install pyttsx3
         
### Importing libraries

         import speech_recognition as spr 
         import pyttsx3 
         
Note that we installed pyaudio but not importing it.
 
         r = sr.Recognizer()
         
Initialize the recognizer

         def SpeakText(command): 
             engine = pyttsx3.init() 
             engine.say(command)  
             engine.runAndWait() 
             
Function to convert text to speech!

         while(1):     
      
Exception handling to handle exceptions at the runtime 

             try: 
          
use the microphone as source for input. 

                 with sr.Microphone() as source2: 
              
wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level.

                     r.adjust_for_ambient_noise(source2, duration=0.2) 
              
listens for the user's input

                     audio2 = r.listen(source2) 
              
Using ggogle to recognize audio 

                     MyText = r.recognize_google(audio2) 
                     MyText = MyText.lower() 
  
                     print("Did you say "+MyText) 
                     SpeakText(MyText) 
                     
                     except sr.RequestError as e: 
                             print("Could not request results; {0}".format(e)) 
          
                     except sr.UnknownValueError: 
                             print("unknown error occured") 
                     
Loop infinitely for the user to speak.
