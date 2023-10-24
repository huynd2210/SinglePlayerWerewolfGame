import random

from src.Common import Utility
from src.NPC import NPC
from src.Npc import Alignment


def isThisNpcAllowedToAct(gameInfo, selfNPC: NPC, possibleTargets):
    if len(possibleTargets) == 0:
        Utility.logDebug("Doctor: No possible targets")
        return False

    if selfNPC.isBeingSuppressed:
        Utility.logDebug("Doctor: NPC is being suppressed")
        return False

    return True

def doctorPossibleTarget(gameInfo, selfNPC: NPC):
    return [npc for npc in gameInfo.npcList if npc.isAlive and npc != selfNPC]

def doctorActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = doctorPossibleTarget(gameInfo, selfNPC)
    chosenTarget = random.choice(list(filter(lambda npc: npc != selfNPC, possibleTargets)))
    if not isThisNpcAllowedToAct(gameInfo, selfNPC, possibleTargets):
        return

    doctorActionFunction(gameInfo, chosenTarget, selfNPC)

# The doctor can save a villager even if the villager is targeted by multiple hostiles
def doctorActionFunction(gameInfo, targetNpc: NPC, selfNPC: NPC):
    if targetNpc not in gameInfo.npcList:
        raise Exception(targetNpc.name + " not found.")

    Utility.logDebug("Doctor: Visiting " + targetNpc.name + " the " + targetNpc.role.roleName)
    selfNPC.isAtHome = False

    if targetNpc.isBeingAmbushed:
        selfNPC.journal.append("visited " + targetNpc.name + " on night " + str(gameInfo.currentTurn))
        resolveVisitingAmbushedNPC(targetNpc)
        return

    if gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled == True and\
            gameInfo.npcList[gameInfo.npcList.index(targetNpc)].role.alignment == Alignment.good:
        selfNPC.journal.append(
            "visited " + targetNpc.name + " on night " + str(gameInfo.currentTurn) + " and saved his life")
        gameInfo.npcList[gameInfo.npcList.index(targetNpc)].isBeingKilled = False
    else:
        selfNPC.journal.append("visited " + targetNpc.name + " on night " + str(gameInfo.currentTurn))


def resolveVisitingAmbushedNPC(targetNPC: NPC, selfNPC: NPC):
    selfNPC.isFreshlyKilled = True
    targetNPC.isBeingAmbushed = False