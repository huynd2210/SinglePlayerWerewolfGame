# from src import PlayerActionList
from src import PlayerActionList
from src.PlayerAction import PlayerAction


class Player:
    def __init__(self, name: str):
        self.name = name
        self.actions = []
        self.initAction()
    def initAction(self):
        self.actions.append(PlayerAction("visit", True, PlayerActionList.visitAction))
        self.actions.append(PlayerAction("execute", False, PlayerActionList.executeNPCAction))
        self.actions.append(PlayerAction("investigate role", False, PlayerActionList.roleInvestigationAction))

    #todo: refactor so that actions can be performed on dead NPCs as well as alive ones, depending on the action
    def takeDayActionDialogue(self, gameInfo):
        print("What do you want to do today? Possible actions are: ")
        possibleDayActions = [actions for actions in self.actions if not actions.isNightAction]
        possibleDayActionsNames = [actions.name for actions in possibleDayActions]
        for action in possibleDayActions:
            print("-- ", action.name)
        actionToTake = input()
        while actionToTake not in possibleDayActionsNames:
            print("Invalid input, try again")
            print("What do you want to do today?")
            for action in possibleDayActions:
                print(action.name)
            actionToTake = input()

        for action in possibleDayActions:
            if action.name == actionToTake:
                action.performAction(gameInfo)

    def takeNightActionDialogue(self, gameInfo):
        print("What do you want to do tonight? Possible actions are: ")
        possibleNightActions = [actions for actions in self.actions if actions.isNightAction]
        possibleNightActionsNames = [actions.name for actions in possibleNightActions]
        for action in possibleNightActions:
            print("-- " + action.name)
        actionToTake = input()
        while actionToTake not in possibleNightActionsNames:
            print("Invalid input, try again")
            print("What do you want to do tonight?")
            for action in possibleNightActions:
                print(action.name)
            actionToTake = input()

        for action in possibleNightActions:
            if action.name == actionToTake:
                action.performAction(gameInfo)


    def printAliveNpcNames(self, aliveNpcNames):
        for npcName in aliveNpcNames:
            print(npcName)