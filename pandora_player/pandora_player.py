from subprocess import PIPE, Popen
import time
import shlex
import platform


class PandoraPlayer():
    def __init__(self):
        shell_command = shlex.split(
            "pianobar", posix=platform.system() != "Windows")
        self.player = Popen(shell_command, stdin=PIPE, stdout=PIPE)
        self.first_start = True

    def play(self):
        if self.player.poll() is None:
            if self.first_start:
                self.player.stdin.write(b'0\n')
                self.first_start = False
            else:
                self.player.stdin.write(b'p\n')
            self.player.stdin.flush()
        else:
            raise ProgramCommunicationError("Couldn't talk to Pianobar")
        return True

    def stop(self):
        if self.player.poll() is None:
            self.player.stdin.write(b'p\n')
            self.player.stdin.flush()
        else:
            raise ProgramCommunicationError("Couldn't pause Pianobar")
        return True

    def close(self):
        if not self.polite_close():
            self.brutal_close()

    def polite_close(self):
        self.player.terminate()
        countdown = 5
        while self.player.poll() is None:
            if countdown <= 0:
                return False
            time.sleep(0.1)
            countdown = countdown - 0.1
        return True

    def brutal_close(self):
        self.player.kill()
        self.player.wait()


class ProgramCommunicationError(Exception):
    def __init__(self, commFailure):
        self.commFailure = commFailure

    def __str__(self):
        return "failed to send message because of {}".format(self.commFailure)
