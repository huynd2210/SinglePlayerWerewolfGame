import random

from src.Common import Utility
from src.NPC import NPC
from src.Npc import Faction

def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):
    if len(possibleTargets) == 0:
        Utility.logDebug("Serial Killer: " + selfNPC.name + " No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Serial Killer: " + selfNPC.name + " NPC is being suppressed")
        return False

    return True

def serialKillerActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = serialKillerPossibleTarget(gameInfo, selfNPC)

    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

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

    Utility.logDebug("Serial Killer: Visiting " + targetNpc.name + " the " + targetNpc.role.roleName)

    gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = True
