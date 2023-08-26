class PlayerAction:
    def __init__(self, name: str, actionFunction):
        self.name = name
        self.actionFunction = actionFunction

    def performAction(self, *args):
        self.actionFunction(*args)


