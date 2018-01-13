from pandora_player.pandora_player import PandoraPlayer


class ActionHandler():
    def __init__(self):
        self.player = PandoraPlayer()

    def take_action(self, action_string):
        if "play pandora" in action_string:
            return self.player.play()
        raise UndefinedCommandError()


class UndefinedCommandError(Exception):
    pass
