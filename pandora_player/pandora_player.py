from subprocess import PIPE, Popen
import time


class PandoraPlayer():
    def __init__(self):
        pass

    def play(self):
        pianobar = Popen(["pianobar"], stdin=PIPE, stdout=PIPE)
        time.sleep(5)
        print(pianobar.stdout.readline())
        pianobar.stdin.write(b'0\n')
        pianobar.stdin.flush()
        return True
