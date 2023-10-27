from src import Player
from src.GameEngine import Game
from src.Npc import RoleActionList

def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
    #game.gameInfo.currentNightType = 'full moon'
    return game

def testPlayerVisitOnVillager():
    game = initSampleGame()
    player = game.gameInfo.player
    npcName = "villagerNPC"
    game.addNPC(npcName, "Villager")
    villager = game.gameInfo.npcList[0]
    actionToTest = player.findActionByName("visit").performAction(game.gameInfo, villager)

    successMessage = "You think that " + npcName + " is a villager."

    assert actionToTest.performAction(game.gameInfo) == successMessage