import random

from src.Common import Utility
from src.NPC import NPC


def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):
    if len(possibleTargets) == 0:
        Utility.logDebug("Trapper: No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Trapper: NPC is being suppressed")
        return False

    return True

def trapperPossibleTarget(gameInfo):
    return [npc for npc in gameInfo.npcList if npc.isAlive]

def trapperActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = trapperPossibleTarget(gameInfo)

    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    trapperActionFunction(gameInfo, chosenTarget, selfNPC)

def trapperActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    Utility.logDebug("Trapper: Visiting " + targetNpc.name + " the " + targetNpc.role.roleName)

    targetNpc.isBeingTrapped = True
    selfNPC.isAtHome = False
