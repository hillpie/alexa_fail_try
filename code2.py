import speech_recognition
import wikipedia
= wikipedia.summary(person, 1)
        print(info)
        talk(info)def take_command():
    try:
        with speech_recognition.Microphone() as source:
            print ('listening...')
            voice = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command