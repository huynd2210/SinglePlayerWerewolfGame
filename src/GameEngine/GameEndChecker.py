from src.GameEngine.Game import Game


def checkAllEvilFactionDead(game: Game) -> bool:
    for npc in game.gameInfo.npcList:
        if npc.role.alignment.lower() == "evil" and npc.isAlive:
            return False
    return True

def checkAllEvilKillerDead(game: Game) -> bool:
    for npc in game.gameInfo.npcList:
        if npc.role.alignment.lower() == "evil" and npc.role.canKill and npc.isAlive:
            return False
    return True

def checkAllGoodFactionDead(game: Game) -> bool:
    for npc in game.gameInfo.npcList:
        if npc.role.alignment.lower() == "good" and npc.isAlive:
            return False
    return True

def isPlayerWin(game: Game) -> bool:
    isAllEvilFactionDead = checkAllEvilFactionDead(game)
    isAllEvilKillerDead = checkAllEvilKillerDead(game)
    if isAllEvilFactionDead:
        print("All evil faction are dead. Player Win")
        return True

    if isAllEvilKillerDead:
        print("All evil faction killers are dead, the remaining evil-doer has fled. Player Win")
        return True
    return False

def isPlayerLose(game: Game) -> bool:
    isAllGoodFactionDead = checkAllGoodFactionDead(game)
    if isAllGoodFactionDead:
        print("All good people are dead. Player Lose")
        return True

    return False
