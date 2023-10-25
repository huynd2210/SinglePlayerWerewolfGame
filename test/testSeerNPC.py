from src import Player
from src.GameEngine import Game
from src.Npc import RoleActionList

def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
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

def testSeerActionOnDoctor():
    game = initSampleGame()
    npcDoctor = "doctorNPC"
    game.addNPC(npcDoctor,"doctor")
    game.addNPC("John", "Seer")
    seer = game.gameInfo.npcList[1] #doctor in npcList[0]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcDoctor + " is a doctor"

def testSeerActionOnWerewolf():
    game = initSampleGame()
    npcWerewolf = "werewolfNPC"
    game.addNPC(npcWerewolf, "werewolf")
    game.addNPC("Lisa", "Seer")
    seer = game.gameInfo.npcList[1]  # werewolf in npcList[0]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcWerewolf + " is a werewolf"

# Guard role
def testSeerActionOnGuard():
    game = initSampleGame()
    npcGuard = "guardNPC"
    game.addNPC(npcGuard, "Guard")
    game.addNPC("Lisa", "Seer")
    seer = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcGuard + " is a guard"

# Cleaner role
def testSeerActionOnCleaner():
    game = initSampleGame()
    npcCleaner = "cleanerNPC"
    game.addNPC(npcCleaner, "cleaner")
    game.addNPC("Lisa", "Seer")
    seer = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcCleaner + " is a cleaner"

# Deceiver role
def testSeerActionOnDeceiver():
    game = initSampleGame()
    npcDeceiver = "DeceiverNPC"
    game.addNPC(npcDeceiver, "deceiver")
    game.addNPC("Lisa", "Seer")
    seer = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcDeceiver + " is a deceiver"

# Ambusher role
def testSeerActionOnAmbusher():
    game = initSampleGame()
    npcAmbusher = "AmbusherNPC"
    game.addNPC(npcAmbusher, "Ambusher")
    game.addNPC("Lisa", "Seer")
    seer = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcAmbusher + " is an ambusher"

# serial killer role
def testSeerActionOnSerialKiller():
    game = initSampleGame()
    npcSerialKiller = "serialKillerNPC"
    game.addNPC(npcSerialKiller, "serial killer")
    game.addNPC("Tom", "Seer")
    seer = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcSerialKiller + " is a serial killer"


# Terrorist role (Not implemented yet)
# def testSeerActionOnTerrorist():
#     game = initSampleGame()
#     npcTerrorist = "terroristNPC"
#     game.addNPC(npcTerrorist, "Terrorist")
#     game.addNPC("Jake", "Seer")
#     seer = game.gameInfo.npcList[1]
#     RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
#     assert seer.journal[0] == npcTerrorist + " is a terrorist"

# Trapper role
def testSeerActionOnTrapper():
    game = initSampleGame()
    npcTrapper = "trapperNPC"
    game.addNPC(npcTrapper, "trapper")
    game.addNPC("Jake", "Seer")
    seer = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, seer)
    assert seer.journal[0] == npcTrapper + " is a trapper"