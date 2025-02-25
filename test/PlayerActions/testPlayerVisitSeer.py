from src import Player
from src.GameEngine import Game
from src.PlayerActions import VisitAction


def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
    return game


def testPlayerVisitSeer():
    game = initSampleGame()
    npcName = "seerNpc"
    game.addNPC(npcName, "Seer")
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)
    isSuccess = resultingMessage.startswith(npcName + " revealed that he is a seer, and he has learned that ")
    assert isSuccess is True
