import speech_recognition as sr
from command_listener.command_listener import CommandListener
from action_handler.action_handler import ActionHandler, UndefinedCommandError
if __name__ == "__main__":
    my_action_handler = ActionHandler()
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            my_command_listener = CommandListener()
            keep_listening = True
            while(keep_listening):
                try:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    text_of_audio = r.recognize_google(audio)
                    if(my_command_listener.command_word_present(text_of_audio)):
                        command_string = my_command_listener.get_command(
                            text_of_audio)
                        print("command word found and was " + command_string)
                        my_action_handler.take_action(command_string)
                    else:
                        print("no command word relistening")
                except sr.UnknownValueError:
                    print("known problem keep running")
                except UndefinedCommandError:
                    print("Undefined command")
    finally:
        my_action_handler.take_action("kill pandora")
