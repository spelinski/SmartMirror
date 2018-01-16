import unittest
from pandora_player.pandora_player import PandoraPlayer
from pandora_player.pandora_player import ProgramCommunicationError
from unittest.mock import patch, Mock


@patch('platform.system')
@patch('shlex.split')
@patch('subprocess.Popen')
class TestPandoraPlalyer(unittest.TestCase):
    def test_first_play_calls_stdin_write_with_zero(self,
                                                    popen_mock,
                                                    shlex_mock,
                                                    system_mock):
        popen_mock.return_value.poll.return_value = None
        my_pandora_player = PandoraPlayer()
        my_pandora_player.play()
        popen_mock.return_value.stdin.write.assert_called_with(b'0\n')

    def test_second_play_calls_stdin_write_with_p(self,
                                                  popen_mock,
                                                  shlex_mock,
                                                  system_mock):
        popen_mock.return_value.poll.return_value = None
        my_pandora_player = PandoraPlayer()
        my_pandora_player.play()
        my_pandora_player.play()
        popen_mock.return_value.stdin.write.assert_called_with(b'p\n')

    def test_play_raises_assertion_if_process_closed(self,
                                                     popen_mock,
                                                     shlex_mock,
                                                     system_mock):
        popen_mock.return_value.poll.return_value = "fake_value"
        my_pandora_player = PandoraPlayer()
        self.assertRaisesRegex(
            ProgramCommunicationError,
            "failed to send message because of Couldn't talk to Pianobar",
            my_pandora_player.play)

    def test_stop_calls_stdin_write_with_p(self,
                                           popen_mock,
                                           shlex_mock,
                                           system_mock):
        popen_mock.return_value.poll.return_value = None
        my_pandora_player = PandoraPlayer()
        my_pandora_player.stop()
        popen_mock.return_value.stdin.write.assert_called_with(b'p\n')

    def test_stop_raises_assertion_if_process_closed(self,
                                                     popen_mock,
                                                     shlex_mock,
                                                     system_mock):
        popen_mock.return_value.poll.return_value = "fake_value"
        my_pandora_player = PandoraPlayer()
        self.assertRaisesRegex(
            ProgramCommunicationError,
            "failed to send message because of Couldn't pause Pianobar",
            my_pandora_player.stop)

    def test_close_with_a_closed_program_only_calls_terminate(self,
                                                              popen_mock,
                                                              shlex_mock,
                                                              system_mock):
        popen_mock.return_value.poll.return_value = "fake_value"
        my_pandora_player = PandoraPlayer()
        my_pandora_player.close()
        self.assertTrue(popen_mock.return_value.terminate.called)
        self.assertFalse(popen_mock.return_value.kill.called)

    @patch('time.sleep')
    def test_close_with_a_program_that_wont_close_calls_kill(self,
                                                             sleep_mock,
                                                             popen_mock,
                                                             shlex_mock,
                                                             system_mock):
        popen_mock.return_value.poll.return_value = None
        my_pandora_player = PandoraPlayer()
        my_pandora_player.close()
        self.assertTrue(popen_mock.return_value.kill.called)
