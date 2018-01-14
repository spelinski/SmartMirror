class ActionHandler():
    def __init__(self, music_player):
        self.player = music_player

    def take_action(self, action_string):
        if "play pandora" in action_string:
            return self.player.play()
        elif "stop pandora" in action_string:
            return self.player.stop()
        elif "kill pandora" in action_string:
            return self.player.close()
        raise UndefinedCommandError()


class UndefinedCommandError(Exception):
    pass
