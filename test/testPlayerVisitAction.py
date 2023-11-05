from src import Player
from src.GameEngine import Game
from src.Npc import RoleActionList
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

def testPlayerVisitOnWerewolfNormalNight():
    game = initSampleGame()
    npcName = "werewolfNPC"
    game.addNPC(npcName, "Werewolf")
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)
    successMessage = "You think that " + npcName + " is a villager."
    assert successMessage == resultingMessage

def testPlayerVisitOnWerewolfFullMoonNight():
    game = initSampleGame()

    #set fuil moon night
    game.gameInfo.currentNightType = 'full moon'

    npcName = "werewolfNPC"
    game.addNPC(npcName, "Werewolf")
    resultingMessage = VisitAction._resolveVisitAction(game.gameInfo, npcName)

    successMessage = npcName + " is not at home. There are traces of wolf fur on the floor. You conclude that he is a werewolf."

    assert successMessage == resultingMessage
