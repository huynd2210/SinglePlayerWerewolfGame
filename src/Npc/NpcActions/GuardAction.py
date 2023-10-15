import random

from src.Common import Utility
from src.NPC import NPC
from src.Npc import Faction

def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):
    if len(possibleTargets) == 0:
        Utility.logDebug("Guard: " + selfNPC.name + " No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Guard: " + selfNPC.name + " NPC is being suppressed")
        return False

    return True

def guardActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = guardPossibleTarget(gameInfo, selfNPC)

    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

    chosenTarget = random.choice(possibleTargets)

    guardActionFunction(gameInfo, chosenTarget, selfNPC)


def guardPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC and not npc.isBeingGuarded]


def guardActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    Utility.logDebug("Guard: Visiting " + targetNpc.name + " the " + targetNpc.role.roleName)
    targetNpc.isBeingGuarded = True
    selfNPC.guarding.append(targetNpc.name)