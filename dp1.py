from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()


class rcvp:
    def action(self):
        print("The person who recieves information")


class invp:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    recv = rcvp()
    cmd = ConcreteCommand(recv)
    inv = invp()
    inv.command(cmd)
    inv.execute()
