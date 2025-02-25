from src import Player
from src.GameEngine import Game
from src.PlayerActions import VisitAction


def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
    return game

def testPlayerVisitSerialKillerAtHome():
    game = initSampleGame()
    npcName = "serialKillerNpc"
    game.addNPC(npcName, "Serial Killer")
    #set npc to be at home
    game.gameInfo.findNpcByName(npcName).isAtHome = True
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)
    successMessage = npcName + " is highly suspicious, you think that he is potentially a criminal"
    assert successMessage == resultingMessage

def testPlayerVisitSerialKillerNotHome():
    game = initSampleGame()
    npcName = "serialKillerNpc"
    game.addNPC(npcName, "Serial Killer")
    #set npc to not be at home
    game.gameInfo.findNpcByName(npcName).isAtHome = False
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)
    successMessage = "You knocked on the door, but it seems that nobody is at home right now"
    assert successMessage == resultingMessage