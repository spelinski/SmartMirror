import re


class CommandListener():
    def __init__(self):
        self.command_word = "mirror"

    def command_word_present(self, user_sentence):
        return self.command_word in user_sentence.lower()

    def get_command(self, user_sentence):
        user_sentence = user_sentence.lower()
        return re.sub('.*' + self.command_word + '\s*', '', user_sentence)
