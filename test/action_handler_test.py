import unittest
from action_handler.action_handler import ActionHandler, UndefinedCommandError
from unittest.mock import patch

class TestActionHandler(unittest.TestCase):
    @patch('pandora_player.pandora_player.PandoraPlayer')
    def test_take_action_doesnt_exist(self, MockPandoraPlayer):
        current_action_handler = ActionHandler(MockPandoraPlayer)
        with self.assertRaises(UndefinedCommandError):
            current_action_handler.take_action("jump up and down")

    @patch('pandora_player.pandora_player.PandoraPlayer')
    def test_play_pandora_calls_player_function_named_play(self, MockPandoraPlayer):
        current_action_handler = ActionHandler(MockPandoraPlayer)
        try:
            current_action_handler.take_action("play pandora")
            self.assertTrue(MockPandoraPlayer.play.called)
        except UndefinedCommandError:
            self.fail("problem with play pandora action")

    @patch('pandora_player.pandora_player.PandoraPlayer')
    def test_stop_pandora_calls_player_function_named_stop(self, MockPandoraPlayer):
        current_action_handler = ActionHandler(MockPandoraPlayer)
        try:
            current_action_handler.take_action("stop pandora")
            self.assertTrue(MockPandoraPlayer.stop.called)
        except UndefinedCommandError:
            self.fail("problem with stop pandora action")

    @patch('pandora_player.pandora_player.PandoraPlayer')
    def test_kill_pandora_calls_player_function_named_close(self, MockPandoraPlayer):
        current_action_handler = ActionHandler(MockPandoraPlayer)
        try:
            current_action_handler.take_action("kill pandora")
            self.assertTrue(MockPandoraPlayer.close.called)
        except UndefinedCommandError:
            self.fail("problem with kill pandora action")
