class Role:
    def __init__(self, roleName : str, faction : str, alignment: str, canKill: bool = False):
        self.roleName = roleName
        self.faction = faction
        self.alignment = alignment
        # For now this boolean is used to check for end condition.
        self.canKill = canKill

    def __repr__(self):
        return self.roleName + " " + self.faction + " " + self.alignment

    def __str__(self):
        return self.roleName + " " + self.faction + " " + self.alignment