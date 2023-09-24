class PlayerAction:
    def __init__(self, name: str, isNightAction, actionFunction, description=""):
        self.name = name
        self.actionFunction = actionFunction
        self.isNightAction = isNightAction
        self.description = description
    def performAction(self, *args):
        return self.actionFunction(*args)


