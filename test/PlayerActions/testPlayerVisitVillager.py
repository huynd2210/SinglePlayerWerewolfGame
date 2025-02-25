from src import Player
from src.GameEngine import Game
from src.PlayerActions import VisitAction


def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
    return game

def testPlayerVisitOnVillager():
    game = initSampleGame()
    npcName = "villagerNPC"
    game.addNPC(npcName, "Villager")
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)
    successMessage = "You think that " + npcName + " is a villager."

    assert successMessage == resultingMessage