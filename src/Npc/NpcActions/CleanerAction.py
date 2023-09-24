import random

from src.Common import Utility
from src.NPC import NPC

def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):

    if len(possibleTargets) == 0:
        Utility.logDebug("Cleaner: No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Cleaner: NPC is being suppressed")
        return False

    return True


def cleanerPossibleTarget(gameInfo):
    return [npc for npc in gameInfo.npcList if not npc.isAlive]

def cleanerActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = cleanerPossibleTarget(gameInfo)

    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    cleanerActionFunction(gameInfo, chosenTarget, selfNPC)

def cleanerActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    if targetNpc.isAlive:
        raise Exception("Cannot cleanup " + targetNpc.name + " as they are still alive")

    # targetNpc.role.roleName = "Cleaned"
    # targetNpc.role.alignment = "Cleaned"
    # targetNpc.role.faction = "Cleaned"

    Utility.logDebug("Cleaner: targeting " + targetNpc.name + " the " + targetNpc.role.roleName)

    targetNpc.isCleaned = True
    targetNpc.journal.clear()
    selfNPC.isAtHome = False

