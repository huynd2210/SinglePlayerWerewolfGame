from src.PlayerActions import VisitAction, ExecuteAction, RoleInvestigationAction, RetrieveJournalAction

visitAction = VisitAction.visitActionWrapper
executeNPCAction = ExecuteAction.executeNPCActionWrapper
# investigate role: Investigate a Npc to find out his role. Note to self: this action can be essentially removed by the cleaner-evil role
roleInvestigationAction = RoleInvestigationAction.roleInvestigationActionWrapper
retrieveJournalAction = RetrieveJournalAction.retrieveJournalActionWrapper
# todo: autopsyAction: Perform autopsy on a dead Npc to find out the cause of death

