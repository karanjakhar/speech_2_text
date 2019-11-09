import speech_recognition as sr


recognizer = sr.Recognizer()
microphone = sr.Microphone()




def microphone_recog():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print('listening...')
        audio = recognizer.listen(source)
        print('processing...')
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return 'speak again'
        print(text)
        return text



def audio_file(file):
    with sr.AudioFile(file) as source:
        r.adjust_for_ambient_noise(source)
        audio_listened = r.listen(source)

        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return 'speak again'
        print(text)
        return text
