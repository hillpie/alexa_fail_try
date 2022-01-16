import datetime

import pyjokes


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'who the hell is' in command:
        person = command.replace('who the hell is', '')
        info
    elif 'date' in command:
        talk('sorry, no')
    elif 'are you single' in command:
        talk('im in relationship with myself')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')

while True:
    run_alexa()