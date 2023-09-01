from src.GameEngine.Game import Game
from src.NPC import RoleActionList
from src.Player import Player


def initSampleGame():
    player = Player("Player")
    game = Game(player, isTestGame=True)
    return game
def testSeerActionOnVillager():
    game = initSampleGame()
    villagerName = "villagerNPC"
    game.addNPC(villagerName, "Villager")
    game.addNPC("Ben", "Seer")
    seer = game.gameInfo.npcList[1]
    villager = game.gameInfo.npcList[0]
    RoleActionList.roleActionMap[seer.role.roleName.lower()](game.gameInfo, villager, seer)
    assert seer.journal[0] == villagerName + " is a villager"

def testDoctorActionJournal():
    game = initSampleGame()
    game.addNPC("villagerNPC", "Villager")
    game.addNPC("doctorNPC", "Doctor")
    villager = game.gameInfo.npcList[0]
    doctor = game.gameInfo.npcList[1]
    RoleActionList.roleActionMap[doctor.role.roleName.lower()](game.gameInfo, villager, doctor)
    assert len(doctor.journal) > 0

def testDoctorSaving():
    game = initSampleGame()
    game.addNPC("villagerNPC", "Villager")
    game.addNPC("doctorNPC", "Doctor")
    game.addNPC("werewolfNPC", "Werewolf")
    game.gameInfo.currentNightType = 'full moon'
    villager = game.gameInfo.npcList[0]
    doctor = game.gameInfo.npcList[1]
    werewolf = game.gameInfo.npcList[2]
    RoleActionList.roleActionMap[werewolf.role.roleName.lower()](game.gameInfo, villager, werewolf)
    assert villager.isBeingKilled == True
    RoleActionList.roleActionMap[doctor.role.roleName.lower()](game.gameInfo, villager, doctor)
    assert villager.isBeingKilled == False
    assert doctor.journal[0] == "visited villagerNPC on night 0 and saved his life"
