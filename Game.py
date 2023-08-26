from GameInfo import GameInfo


class Game:
    def __init__(self, player):
        self.gameInfo = self._initGameInfo(player)

    def _initGameInfo(self, player):
        return GameInfo(player, [])

    def addNPC(self, npc):