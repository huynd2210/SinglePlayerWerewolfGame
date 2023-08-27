import random

import PlayerActionList
import RoleList
from GameEngine import GameConfig
from GameEngine.NightInfo import NightInfo
from GameEngine.GameInfo import GameInfo
from NPC import NPC
from NPCActions import RoleActionList

class Game:
    def __init__(self, player):
        self.gameInfo = self._initGameInfo(player)
        self.nightInfo = self._initNightInfo()
        self.configMap = self._initConfigMap()
        self.initTestGame()
    def _initNightInfo(self):
        return NightInfo()

    def _initGameInfo(self, player):
        return GameInfo(player, [])

    def _initConfigMap(self):
        return {
            "seer": {
                "actFrequency": GameConfig.seerActFrequency,
            },
            "doctor": {
                "actFrequency": GameConfig.doctorActFrequency,
            },
            "villager": {
                "actFrequency": GameConfig.villagerActFrequency,
            },
            "werewolf": {
                "actFrequency": GameConfig.werewolfActFrequency,
            },

        }

    def addNPC(self, name, roleName):
        role = RoleList.roleMap[roleName.lower()]
        self.gameInfo.npcList.append(NPC(role, name))

    def initTestGame(self):
        self.addNPC("Tim", "Villager")
        self.addNPC("Tom", "Villager")
        self.addNPC("Bob", "Villager")
        self.addNPC("Ben", "Seer")
        self.addNPC("Bad Guy", "Werewolf")
    def countRoles(self):
        roleCount = {}
        for npc in self.gameInfo.npcList:
            if npc.role.roleName not in roleCount:
                roleCount[npc.role.roleName] = 1
            else:
                roleCount[npc.role.roleName] += 1
        return roleCount

    def firstDayBriefing(self, villageName):
        print(
            "Welcome to village " + villageName + ". You are to root out the evil that has been plaguing this village.")
        print("Your informants have told you that there are " + str(
            len(self.gameInfo.npcList)) + " people in this village.")
        print("The village has: ")
        for role, count in self.countRoles().items():
            print(str(count) + " " + role + "(s)")
        print("Good luck and execute the will of the Emperor!")
        print("================================================")

    # Execute all evil factions to win
    def isPlayerWin(self):
        # return sum(
        #     map(lambda npc: npc.role.alignment.lower() == "evil" and not npc.isAlive, self.gameInfo.npcList)) == 0
        for npc in self.gameInfo.npcList:
            if npc.role.alignment.lower() == "evil" and npc.isAlive:
                return False
        return True

    # change from 0 to other numbers
    def isPlayerLose(self):
        return sum(map(lambda npc: npc.role.alignment.lower() == "good" and npc.isAlive, self.gameInfo.npcList)) == 0

    def isGameOver(self):
        return self.isPlayerWin() or self.isPlayerLose()

    def startGame(self):
        villageName = "Doomed Village"
        while not self.isGameOver():
            self.gameInfo.currentTurn += 1
            print("Day " + str(self.gameInfo.currentTurn))
            self._dayPhase(villageName)
            print("Night " + str(self.gameInfo.currentTurn))
            self._nightPhase()

    def _dayPhase(self, villageName):
        if self.gameInfo.currentTurn == 1:
            self.firstDayBriefing(villageName)
        else:
            # Announce who died
            self.announceNightCasualties()

            # Player perform day actions
            self.playerDayAction()
            # End day phase

    def _nightPhase(self):
        #First, the npc will act
        if self.gameInfo.currentNightType.lower() == 'normal':
            print("Tonight is quiet")
        elif self.gameInfo.currentNightType.lower() == 'full moon':
            print("Tonight is full moon")

        for npc in self.gameInfo.npcList:
            if npc.isAlive and npc.isAllowedToAct:
                self.npcNightAction(npc)
        self.updateGameInfo()
        #Then the player will act
        self.playerNightAction()

    def announceNightCasualties(self):
        print(str(len(self.nightInfo.nightCasualties)) + " people died last night.")
        print("The dead are: ")
        for npc in self.nightInfo.nightCasualties:
            print(npc.name)
        self.nightInfo.reset()

    # todo: refactor this for more actions in the future
    def playerDayAction(self):
        # execute NPC
        print("Who do you want to execute?")
        aliveNpc = list(filter(lambda npc: npc.isAlive, self.gameInfo.npcList))
        for npc in aliveNpc:
            print(npc.name)
        npcToExecute = input()

        aliveNpcNameList = [npc.name for npc in aliveNpc]

        while npcToExecute not in aliveNpcNameList:
            if npcToExecute == "None":
                break
            print("Invalid input, try again")
            print("Who do you want to execute?")
            for npc in aliveNpc:
                print(npc.name)
            npcToExecute = input()

        if npcToExecute != "None":
            PlayerActionList.executeNPCAction(self.gameInfo, npcToExecute)

    def playerNightAction(self):
        self.gameInfo.player.takeNightActionDialogue(self.gameInfo)

    def npcNightAction(self, npc):
        targetNpc = self.chooseTargetNpc(npc)
        RoleActionList.roleActionMap[npc.role.roleName.lower()](self.gameInfo, targetNpc, npc)

    # This function controls the NPC's behavior
    def updateGameInfo(self):
        for npc in self.gameInfo.npcList:
            if self.gameInfo.currentTurn % self.configMap[npc.role.roleName.lower()]["actFrequency"] == 0:
                npc.isAllowedToAct = True

        if self.gameInfo.currentNightType.lower() == "full moon":
            self.gameInfo.currentNightType = "normal"

        if self.gameInfo.currentNightType.lower() == "normal" and self.gameInfo.currentTurn % GameConfig.fullMoonFrequency == 0:
            self.gameInfo.currentNightType = "full moon"

    # This function allows the NPC to choose a target based on some criteria (todo)
    def chooseTargetNpc(self, originNpc):
        aliveNpc = list(filter(lambda npc: npc.isAlive, self.gameInfo.npcList))
        return random.choice(list(filter(lambda npc: npc != originNpc, aliveNpc)))
