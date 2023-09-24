import random
from src.NPC import NPC
from src.Npc import Faction


def serialKillerActionWrapper(gameInfo, selfNPC: NPC):
    if selfNPC.isBeingSuppressed:
        return
    possibleTargets = serialKillerPossibleTarget(gameInfo, selfNPC)
    commonerTargets = [npc for npc in possibleTargets if npc.role.faction == Faction.commoner]
    targetingFrequency = 0.8
    if commonerTargets and random.random() < targetingFrequency:
        chosenTarget = random.choice(commonerTargets)
    else:
        chosenTarget = random.choice(possibleTargets)
    serialKillerActionFunction(gameInfo, chosenTarget)


def serialKillerPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC and npc.role.faction != Faction.beast]


def serialKillerActionFunction(gameInfo, targetNpc: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = True
