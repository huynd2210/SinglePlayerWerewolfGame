from src import Player
from src.GameEngine import Game
from src.Npc import RoleActionList

def initSampleGame():
    player = Player.Player("Player")
    game = Game.Game(player, isTestGame=True)
    game.gameInfo.currentNightType = "full moon".lower()
    return game

# Villager role
def testWerewolfOnVillager():
    game = initSampleGame()
    npcVillager = "villagerNPC"
    game.addNPC(npcVillager, "Villager")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True

# Guard role
def testWerewolfOnGuard():
    game = initSampleGame()
    npcVillager = "villagerNPC"
    game.addNPC(npcVillager, "Villager")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True

# Doctor role
def testWerewolfOnDoctor():
    game = initSampleGame()
    npcDoctor = "doctorNPC"
    game.addNPC(npcDoctor, "doctor")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True

# Cleaner role
def testWerewolfOnCleaner():
    game = initSampleGame()
    npcCleaner = "cleanerNPC"
    game.addNPC(npcCleaner, "cleaner")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True

# Deceiver role
def testWerewolfOnDeceiver():
    game = initSampleGame()
    npcDeceiver = "deceiverNPC"
    game.addNPC(npcDeceiver, "deceiver")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True

# Ambusher role
def testWerewolfOnAmbusher():
    game = initSampleGame()
    npcAmbusher = "ambusherNPC"
    game.addNPC(npcAmbusher, "Ambusher")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True

# Serial Killer role
def testWerewolfOnSerialKiller():
    game = initSampleGame()
    npcSerialKiller = "serialKillerNPC"
    game.addNPC(npcSerialKiller, "serial killer")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True

# Trapper role
def testWerewolfOnTrapper():
    game = initSampleGame()
    npcTrapper = "trapperNPC"
    game.addNPC(npcTrapper, "trapper")
    game.addNPC("Ben", "Werewolf")
    victim = game.gameInfo.npcList[0]
    werewolf = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, werewolf)
    assert victim.isBeingKilled == True
