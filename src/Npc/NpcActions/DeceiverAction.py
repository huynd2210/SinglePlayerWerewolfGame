import random

from src.Common import Utility
from src.NPC import NPC
from src.Npc import Faction

def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):
    if len(possibleTargets) == 0:
        Utility.logDebug("Deceiver: No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Deceiver: NPC is being suppressed")
        return False

    return True


def deceiverActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = deceiverPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

    deceiverActionFunction(gameInfo, chosenTarget)

def deceiverPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC and npc.role.faction == Faction.criminal]
def deceiverActionFunction(gameInfo, targetNpc: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    Utility.logDebug("Deceiver: " + targetNpc.name + " is being covered by "
                     + gameInfo.npcList[gameInfo.npcList.index(targetNpc)].name
                     + " the " + targetNpc.role.roleName)
    gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingCoveredByDeceiver = True
