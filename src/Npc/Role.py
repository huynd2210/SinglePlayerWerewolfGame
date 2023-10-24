class Role:
    def __init__(self, roleName : str, faction : str, alignment: str, actionPriority: int = None, canKill: bool = False):
        self.roleName = roleName
        self.faction = faction
        self.alignment = alignment
        # For now this boolean is used to check for end condition.
        self.canKill = canKill

        # Action priority determines who goes first in performing actions. The lower the number, the higher the priority.

        self.actionPriority = actionPriority

    def __repr__(self):
        return self.roleName + " " + self.faction + " " + self.alignment

    def __str__(self):
        return self.roleName + " " + self.faction + " " + self.alignment