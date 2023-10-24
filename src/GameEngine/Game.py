import random

from src.GameEngine import GameConfig, GameEndChecker
from src.GameEngine.NightInfo import NightInfo
from src.GameEngine.GameInfo import GameInfo
from src.NPC import NPC
from src.Npc import RoleList
from src.Npc import RoleActionList

class Game:
    def __init__(self, player, config=None, isTestGame=False, isDebug=False):
        self.gameInfo = self._initGameInfo(player)
        self.nightInfo = self._initNightInfo()
        self.configMap = self._initConfigMap()

        GameConfig.isDebug = isDebug

        if isTestGame == True:
            #If test game is true, then dont setup anything
            return

        if config == None:
            self.initTestGame()
        else:
            self.setupGameWithConfig(config)

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
            "trapper": {
                "actFrequency": GameConfig.trapperActFrequency,
            },
            "cleaner": {
                "actFrequency": GameConfig.cleanerActFrequency,
            },
            "deceiver": {
                "actFrequency": GameConfig.deceiverActFrequency,
            },
            "serial killer": {
                "actFrequency": GameConfig.serialKillerActFrequency,
            },
            "guard": {
                "actFrequency": GameConfig.guardActFrequency,
            },
            "ambusher": {
                "actFrequency": GameConfig.ambusherActFrequency,
            },
            "terrorist": {
                "actFrequency": GameConfig.terroristActFrequency,
            }
        }

    def addNPC(self, name, roleName):
        role = RoleList.roleMap[roleName.lower()]
        actionFunction = RoleActionList.roleActionMap[roleName.lower()]
        self.gameInfo.npcList.append(NPC(role, name, actionFunction=actionFunction))

    def setupGameWithConfig(self, setupNPCCounts):
        NPCNames = ["Tim", "Tom", "Tip", "Bob", "Ben", "David", "Chad", "Chen", "Michael",
                    "James", "John", "Deema", "Robert", "William", "Christ", "Joe", "Dan", "Richard", "Thomas", "Jen",
                    "Jenny", "Sarah", "Mike", "Lisa", "Alex", "Chloe", "Dave", "Emily", "Sam", "Lily", "Tom", "Jessica",
                    "Ryan", "Megan", "Andy", "Grace", "Jake", "Liam", "Emma", "Olivia", "Ava", "Isabella", "Sophia",
                    ]
        for role, count in setupNPCCounts.items():
            for _ in range(count):
                name = random.choice(NPCNames)
                NPCNames.remove(name)
                self.addNPC(name, role)

        random.shuffle(self.gameInfo.npcList)

    # Not yet implemented
    def setupGameRandom(self):
        pass

    def initTestGame(self):
        self.addNPC("Tim", "Villager")
        self.addNPC("Tom", "Villager")
        self.addNPC("Bob", "Villager")
        self.addNPC("Ben", "Seer")
        self.addNPC("Chad", "Werewolf")
        self.addNPC("Trappy", "Trapper")

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
        return GameEndChecker.isPlayerWin(self)

    def isPlayerLose(self):
        return GameEndChecker.isPlayerLose(self)

    def isGameOver(self):
        return self.isPlayerWin() or self.isPlayerLose()

    def startGame(self):
        villageName = "Doomed Village"
        while not self.isGameOver():
            self.gameInfo.currentTurn += 1
            print("Day " + str(self.gameInfo.currentTurn))
            self._dayPhase(villageName)

            if self.isGameOver():
                break

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

    def _nightPhase(self):
        # First, the npc will act
        if self.gameInfo.currentNightType.lower() == 'normal':
            print("Tonight is quiet")
        elif self.gameInfo.currentNightType.lower() == 'full moon':
            print("Tonight is full moon")

        self.resolveNPCNightActions()

        # Then the player will act
        self.playerNightAction()
        self.updateGameInfo()

    def resolveNPCNightActions(self):
        npcsThatWillAct = []
        for npc in self.gameInfo.npcList:
            if npc.isAlive and npc.isAllowedToAct:
                # self.npcNightAction(npc)
                npcsThatWillAct.append(npc)

    def announceNightCasualties(self):
        print(str(len(self.nightInfo.nightCasualties)) + " people died last night.")
        if len(self.nightInfo.nightCasualties) > 0:
            print("The dead are: ")
        for npc in self.nightInfo.nightCasualties:
            print(npc.name)
        self.nightInfo.reset()

    def playerDayAction(self):
        self.gameInfo.player.takeDayActionDialogue(self.gameInfo)

    def playerNightAction(self):
        self.gameInfo.player.takeNightActionDialogue(self.gameInfo)

    def npcNightAction(self, npc):
        # targetNpc = self.chooseTargetNpc(npc)
        RoleActionList.roleActionMap[npc.role.roleName.lower()](self.gameInfo, npc)

    # This function controls the Npc's behavior
    def updateGameInfo(self):
        self.updateNPCStatuses()

        if self.gameInfo.currentNightType.lower() == "full moon":
            self.gameInfo.currentNightType = "normal"

        #since updateGameInfo() will update for the next round, therefore we need add one to self.gameInfo.currentTurn
        if self.gameInfo.currentNightType.lower() == "normal" and (self.gameInfo.currentTurn + 1) % GameConfig.fullMoonFrequency == 0:
            self.gameInfo.currentNightType = "full moon"

        self.nightInfo.resolveNightConclusion(self.gameInfo)


    def updateNPCStatuses(self):
        # Update statuses
        for npc in self.gameInfo.npcList:
            npcRole = npc.role.roleName.lower()
            if self.gameInfo.currentTurn % self.configMap[npcRole]["actFrequency"] == 0:
                npc.isAllowedToAct = True
            else:
                npc.isAllowedToAct = False

            npc.isBeingTrapped = False
            npc.isAtHome = True
            npc.isBeingCoveredByDeceiver = False
            npc.isBeingSuppressed = False
            npc.isBeingGuarded = False
            npc.isFreshlyKilled = False


    # This function allows the Npc to choose a target based on some criteria (todo)
    def chooseTargetNpc(self, originNpc):
        aliveNpc = list(filter(lambda npc: npc.isAlive, self.gameInfo.npcList))
        return random.choice(list(filter(lambda npc: npc != originNpc, aliveNpc)))
