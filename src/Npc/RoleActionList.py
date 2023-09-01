from src.NPC import NPC
import random

from src.Npc import Faction, Alignment


# def seerActionFunctionWrapper(gameInfo):

def seerActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = seerPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    seerActionFunction(gameInfo, chosenTarget, selfNPC)
def seerPossibleTarget(gameInfo, selfNPC: NPC):
    # return [gameInfo.npcList[npc].name for npc in range(len(gameInfo.npcList)) if gameInfo.npcList[npc].isAlive]
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC]

def seerActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    if targetNPC not in gameInfo.npcList:
        raise Exception(targetNPC.name + " not found.")

    # selfNPC.journal.append((targetNpcName, gameInfo.npcList[targetNpcName].role.roleName))
    selfNPC.journal.append(targetNPC.name + " is a " + gameInfo.npcList[gameInfo.npcList.index(targetNPC)].role.roleName)

def werewolfActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = werewolfPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    werewolfActionFunction(gameInfo, chosenTarget, selfNPC)

def werewolfPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC and npc.role.faction != Faction.beast]

def werewolfActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    #if not full moon, werewolf does nothing
    if gameInfo.currentNightType == "full moon":
        gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = True

def doctorPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC]

def doctorActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = doctorPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    doctorActionFunction(gameInfo, chosenTarget, selfNPC)


# The doctor can save a villager even if the villager is targeted by multiple hostiles
def doctorActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    if gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled == True and\
            gameInfo.npcList[gameInfo.npcList.index(targetNpc)].role.alignment == Alignment.good:
        selfNPC.journal.append(
            "visited " + targetNpc.name + " on night " + str(gameInfo.currentTurn) + " and saved his life")
        gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = False
    else:
        selfNPC.journal.append("visited " + targetNpc.name + " on night " + str(gameInfo.currentTurn))

#Villagers do nothing
def villagerActionFunction(gameInfo, selfNPC:NPC ):
    pass

def trapperActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    pass

def deceiverActionFunction(gameInfo, targetNPC: NPC, selfNPC: NPC):
    pass

def cleanerActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    if targetNpc.isAlive:
        raise Exception("Cannot cleanup " + targetNpc.name + " as they are still alive")

    targetNpc.role.roleName = "Cleaned"
    targetNpc.role.alignment = "Cleaned"
    targetNpc.role.faction = "Cleaned"
    targetNpc.journal.clear()

roleActionMap = {
    "seer": seerActionWrapper,
    "werewolf": werewolfActionWrapper,
    "doctor": doctorActionWrapper,
    "villager": villagerActionFunction,
    "trapper": trapperActionFunction,
    "deceiver": deceiverActionFunction,
    "cleaner": cleanerActionFunction,
}
