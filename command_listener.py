class CommandListener():
    def __init__(self):
        self.command_word = "mirror"

    def command_word_present(self, user_sentence):
        return self.command_word in user_sentence.lower()
