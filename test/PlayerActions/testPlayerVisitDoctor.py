from src import Player
from src.GameEngine import Game
from src.PlayerActions import VisitAction


def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
    return game

def testPlayerVisitDoctorAtHome():
    game = initSampleGame()
    npcName = "doctorNpc"
    game.addNPC(npcName, "Doctor")
    #set npc to be at home
    game.gameInfo.findNpcByName(npcName).isAtHome = True
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)
    isSuccess = resultingMessage.startswith(npcName + " revealed that he is a doctor and he")
    assert isSuccess

def testPlayerVisitDoctorNotHome():
    game = initSampleGame()
    npcName = "doctorNpc"
    game.addNPC(npcName, "Doctor")
    #set npc to not be at home
    game.gameInfo.findNpcByName(npcName).isAtHome = False
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)
    successMessage = "You knocked on the door, but it seems that nobody is at home right now"
    assert successMessage == resultingMessage