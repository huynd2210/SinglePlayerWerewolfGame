from src import PlayerActionList
from src.PlayerAction import PlayerAction


class Player:
    def __init__(self, name: str):
        self.name = name
        self.actions = []
        self.inventory = {}
        self.initAction()
    def initAction(self):
        self.actions.append(PlayerAction("visit", True, PlayerActionList.visitAction, "Visit an NPC in order to investigate their role"))
        self.actions.append(PlayerAction("execute", False, PlayerActionList.executeNPCAction, "Execute an NPC"))
        self.actions.append(PlayerAction("investigate role", False, PlayerActionList.roleInvestigationAction, "Investigate the role of a dead NPC"))
        self.actions.append(PlayerAction("retrieve journal", False, PlayerActionList.retrieveJournalAction, "Retrieve the journal of a dead NPC"))
        self.actions.append(PlayerAction("suppress", False, PlayerActionList.suppressAction, "Lockdown an NPC, preventing them from performing actions"))


    def takeDayActionDialogue(self, gameInfo):
        print("What do you want to do today? Possible actions are: ")
        possibleDayActions = [actions for actions in self.actions if not actions.isNightAction]

        for i in range(len(possibleDayActions)):
            print(i, "--", possibleDayActions[i].name, ":", possibleDayActions[i].description)

        print(len(possibleDayActions) ,"-- nothing")

        action = self._takeActionInput(possibleDayActions)
        if action == None:
            return
        isActionSuccessful = action.performAction(gameInfo)
        # action was not successfully performed (i.e no targets)
        if isActionSuccessful == False:
            self.takeDayActionDialogue(gameInfo)

    def _takeActionInput(self, possibleActions):
        actionToTake = input()
        isPlayerChoosingNothing = actionToTake.lower() == "nothing" and not actionToTake.isdigit()
        if isPlayerChoosingNothing or int(actionToTake) >= len(possibleActions):
            return

        possibleActionNames = [actions.name for actions in possibleActions]

        while actionToTake not in possibleActionNames and not actionToTake.isdigit():
            print("Invalid input, try again")
            print("What do you want to do tonight?")
            for action in possibleActions:
                print("--", action.name)
            actionToTake = input()
            if actionToTake.lower() == "nothing":
                return

        if actionToTake.isdigit():
            return possibleActions[int(actionToTake)]

        for action in possibleActions:
            if action.name == actionToTake:
                return action

    def takeNightActionDialogue(self, gameInfo):
        print("What do you want to do tonight? Possible actions are: ")
        possibleNightActions = [actions for actions in self.actions if actions.isNightAction]

        for i in range(len(possibleNightActions)):
            print(i, "--", possibleNightActions[i].name, ":", possibleNightActions[i].description)
        #Do nothing
        print(len(possibleNightActions) ,"-- nothing")

        action = self._takeActionInput(possibleNightActions)

        if action == None:
            return

        isActionSuccessful = action.performAction(gameInfo)
        # action was not successfully performed (i.e no targets)
        if isActionSuccessful == False:
            self.takeNightActionDialogue(gameInfo)


    def printAliveNpcNames(self, aliveNpcNames):
        for npcName in aliveNpcNames:
            print(npcName)