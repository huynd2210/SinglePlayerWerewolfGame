from src import Player
from src.GameEngine import Game
from src.Npc import RoleActionList

def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
    #game.gameInfo.currentNightType = 'full moon'
    return game

def testSeerActionOnVillager():
    game = initSampleGame()
    villagerName = "villagerNPC"
    game.addNPC(villagerName, "Villager")
    game.addNPC("Ben", "Seer")
    seer = game.gameInfo.npcList[1]
    # villager = game.gameInfo.npcList[0]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == villagerName + " is a villager"

def testSeerActionWerewolf():
    pass

