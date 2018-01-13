import unittest
from action_handler.action_handler import ActionHandler, UndefinedCommandError


def fakePlayersPlay():
    return "play called"


class TestActionHandler(unittest.TestCase):
    def test_take_action_doesnt_exist(self):
        current_action_handler = ActionHandler()
        with self.assertRaises(UndefinedCommandError):
            current_action_handler.take_action("jump up and down")

    def test_play_pandora_calls_function_named_play_pandora(self):
        current_action_handler = ActionHandler()
        current_action_handler.player.play = fakePlayersPlay
        try:
            self.assertEqual(current_action_handler.take_action(
                "play pandora"), "play called")
        except UndefinedCommandError:
            self.fail("problem with play pandora action")
