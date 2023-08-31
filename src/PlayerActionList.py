from src.PlayerActions import VisitAction, ExecuteAction, RoleInvestigationAction

visitAction = VisitAction.visitActionWrapper
executeNPCAction = ExecuteAction.executeNPCActionWrapper
# investigate role: Investigate a NPC to find out his role. Note to self: this action can be essentially removed by the cleaner-evil role
roleInvestigationAction = RoleInvestigationAction.roleInvestigationActionWrapper
# todo: autopsyAction: Perform autopsy on a dead NPC to find out the cause of death

