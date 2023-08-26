from GameInfo import GameInfo
from NPC import NPC
from Role import Role


class Game:
    def __init__(self, player):
        self.gameInfo = self._initGameInfo(player)

    def _initGameInfo(self, player):
        return GameInfo(player, [])

    def addNPC(self, role, name):
        self.gameInfo.npcList.append(NPC(role, name))

    def countRoles(self):
        roleCount = {}
        for npc in self.gameInfo.npcList:
            if npc.role.roleName not in roleCount:
                roleCount[npc.role.roleName] = 1
            else:
                roleCount[npc.role.roleName] += 1
        return roleCount

    def firstDayBriefing(self, villageName):
        print("Welcome to village " + villageName + ". You are to root out the evil that has been plaguing this village.")
        print("Your informants have told you that there are " + str(len(self.gameInfo.npcList)) + " people in this village.")
        print("The village has: ")
        for role, count in self.countRoles().items():
            print(str(count) + " " + role + "(s)")
        print("Good luck and execute the will of the Emperor!")

    #Execute all evil factions to win
    def isPlayerWin(self):
        return sum(map(lambda npc: npc.role.alignment.lower() == "evil" and not npc.isAlive, self.gameInfo.npcList)) == 0

    #change from 0 to other numbers
    def isPlayerLose(self):
        return sum(map(lambda npc: npc.role.alignment.lower() == "good" and npc.isAlive, self.gameInfo.npcList)) == 0

    def isGameOver(self):
        return self.isPlayerWin() or self.isPlayerLose()
    def startGame(self):
        villageName = "Doomed Village"
        self.firstDayBriefing(villageName)
        while not self.isGameOver():
            self.gameInfo.currentTurn += 1
            print("Day " + str(self.gameInfo.currentTurn))
            self._dayPhase()
            print("Night " + str(self.gameInfo.currentTurn))
            self._nightPhase()

