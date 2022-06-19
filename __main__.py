import speech_recognition as sr

file_name = r'output.wav'

# initialize recognizer
r = sr.Recognizer()

# with sr.AudioFile(file_name) as source:
#     # listen to audio
#     audio_data = r.record(source)

#     # convert audio to text
#     text = r.recognize_google(audio_data)

#     print(text)

with sr.Microphone() as source:
    print('Recording...')
    audio_data = r.listen(source)

    print("Converting...")

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio_data, language="en-US"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
