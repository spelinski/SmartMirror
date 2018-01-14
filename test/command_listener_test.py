import unittest
from command_listener.command_listener import CommandListener


class TestCommandListener(unittest.TestCase):
    def test_detecting_no_command_word(self):
        current_listener = CommandListener()
        self.assertFalse(current_listener.command_word_present(
            "hey do you mind picking up milk"))

    def test_detecting_command_word_at_beginning(self):
        current_listener = CommandListener()
        test_string = current_listener.command_word + \
            " search youtube for starcraft two"
        self.assertTrue(current_listener.command_word_present(test_string))

    def test_detecting_command_word_middle(self):
        current_listener = CommandListener()
        test_string = "thanks just let me know " + \
            current_listener.command_word + " play pandora"
        self.assertTrue(current_listener.command_word_present(test_string))

    def test_getting_command_with_command_word_beginning(self):
        current_listener = CommandListener()
        test_string = current_listener.command_word + \
            " search youtube for starcraft two"
        self.assertEqual(current_listener.get_command(
            test_string), "search youtube for starcraft two")

    def test_getting_command_with_command_word_middle(self):
        current_listener = CommandListener()
        test_string = "thanks just let me know " + \
            current_listener.command_word + " Play pandora"
        self.assertEqual(current_listener.get_command(
            test_string), "play pandora")
