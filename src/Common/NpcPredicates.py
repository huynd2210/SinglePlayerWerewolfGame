def findNpcGuardingNpcByTargetName(gameInfo, kwargs):
    targetNpcName = kwargs["targetNpcName"]
    return [gameInfo.npcList[npc].name for npc in range(len(gameInfo.npcList)) if targetNpcName in gameInfo.npcList[npc].guarding]