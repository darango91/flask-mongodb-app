"""
Workflow helper file

Author: Diego Arango - @darango91
"""

from src.constants import ACTION_STATUS_MSG, NEXT_TARGET_MSG, NO_NEXT_TARGET_MSG, VALID_ACTIONS, VALIDATION_STATUS_MSG
from src.exceptions import AccountNotFound
from src.models import Account
from src.utils import SwitchAction, Validator


class WorkflowHelper:
    """
    Workflow helper class
    """
    workflow = None
    steps = None
    steps_dict = {}
    mongo = None

    action_switcher = SwitchAction()
    validator = Validator()

    def __init__(self, workflow, mongo):
        self.workflow = workflow
        self.mongo = mongo
        self.steps = workflow.get("steps", [])
        for step in self.steps:
            self.steps_dict[step.get("id")] = step

    def process_workflow(self):
        """
        Process the workflow starting from two possible options, a trigger or a start id in the steps
        :return: dict the full workflow dict
        """

        if "trigger" in self.workflow.keys():
            trigger = self.workflow.get("trigger", {})
        else:
            trigger = self.steps_dict.get("start")

        transitions = trigger.get("transitions")
        user_id = trigger.get("params", {}).get("user_id")
        pin = trigger.get("params", {}).get("pin")

        account = self.mongo.db.accounts.find_one({"user_id": user_id})
        if account is None:
            raise AccountNotFound()

        step_params = {
            "user_id": user_id,
            "pin": pin
        }

        account_model = Account(account)

        self.action_switcher.account = account_model
        self.action_switcher.mongo = self.mongo
        self.validator.account = account_model

        target = transitions[0].get("target") if len(transitions) > 0 else None

        while target is not None:
            step = self.steps_dict.get(target)
            step_params.update(step.get("params"))
            target = self.perform_action(step, step_params)

        print(NO_NEXT_TARGET_MSG)
        return None

    def perform_action(self, step, step_params):
        step_action = step.get("action")
        if step_action in VALID_ACTIONS:
            action_result = self.action_switcher.switch(step_action, **step_params)
            print(
                ACTION_STATUS_MSG.format(
                    step.get("id"),
                    step_action,
                    action_result
                )
            )

            step_transitions = step.get("transitions", [])
            if len(step_transitions) == 0:
                return None

            transitions_counter = 0
            for transition in step_transitions:
                target, valid = self.perform_transition(transition, step)
                if len(step_transitions) == transitions_counter+1 or valid:
                    break
                transitions_counter += 1

            return target

    def perform_transition(self, transition, step):
        if len(transition.get("condition", [])) == 0:
            target = transition.get("target")
            print(NEXT_TARGET_MSG.format(target))
            return target, True

        condition = transition.get("condition", [])[0]
        operator = condition.get("operator")
        field_id = condition.get("field_id")
        value = condition.get("value")
        valid = self.validator.validate(
            operator, field_id, value
        )

        print(
            VALIDATION_STATUS_MSG.format(
                step.get("id"),
                field_id,
                operator,
                value,
                valid
            )
        )

        if valid:
            target = transition.get("target")
            print(NEXT_TARGET_MSG.format(target))
            return target, valid

        return None, False
