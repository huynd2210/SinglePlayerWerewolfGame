import random

from src.NPC import NPC


def cleanerPossibleTarget(gameInfo):
    return [npc for npc in gameInfo.npcList if not npc.isAlive]

def cleanerActionWrapper(gameInfo, selfNPC: NPC):
    possibleTargets = cleanerPossibleTarget(gameInfo)
    if len(possibleTargets) == 0:
        return

    if selfNPC.isBeingSuppressed:
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

    targetNpc.isCleaned = True
    targetNpc.journal.clear()
    selfNPC.isAtHome = False

