import speech_recognition as sr
from command_listener import CommandListener
if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        my_command_listener = CommandListener()
        keep_listening = True
        while(keep_listening):
            try:
                audio = r.listen(source)
                text_of_audio = r.recognize_google(audio)
                if(my_command_listener.command_word_present(text_of_audio)):
                    print("command word found exiting")
                    keep_listening = False
                else:
                    print("no command word relistening")
            except sr.UnknownValueError:
                print("known problem keep running")
