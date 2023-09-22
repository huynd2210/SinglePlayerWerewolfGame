class PlayerAction:
    def __init__(self, name: str, isNightAction, actionFunction):
        self.name = name
        self.actionFunction = actionFunction
        self.isNightAction = isNightAction

    def performAction(self, *args):
        return self.actionFunction(*args)


