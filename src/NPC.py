from src.Npc.Role import Role

class NPC:
    #Note, when adding new flags or statuses, make sure to modify updateNPCStatuses.
    def __init__(self, role: Role, name: str, actionFunction):
        self.role = role
        self.name = name
        #Journal is a list that contains information that this npc has learned. For example, the seer can learn other villagers roles and note them here.
        self.journal = []
        self.statuses = []
        self.isAlive = True # Set isAlive =  false in
        self.actionFunction = actionFunction


        #Flag to indicate that this npc is being killed. If this npc is not saved by the end of the night, then he will die.
        self.isBeingKilled = False
        self.isAtHome = True
        self.isAllowedToAct = True
        self.isBeingTrapped = False
        self.isBeingCoveredByDeceiver = False
        self.isCleaned = False
        self.isBeingSuppressed = False
        self.isBeingGuarded = False
        #isFreshlyKilled indicates that this npc is dead during the current night due to other circumstances rather than targeted by killers
        self.isFreshlyKilled = False
        #guarding is for guarding roles, indicate the npcs being guarded by this npc
        self.guarding = []
        #flag for ambusher action
        self.isBeingAmbushed = False
        #flag for terrorist action
        self.isBeingBombed = False

    def __repr__(self):
        return self.name + ": " + str(self.role)

    def performAction(self, *args):
        self.actionFunction(*args)

