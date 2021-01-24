"""
Constants file

Author: Diego Arango - @darango91
"""

API_TEST_TEXT = "I'm here to be tested!"

MONGO_DB_CONNECTION = "mongodb://localhost:27017/playvoxdb"

# Valid actions for the workflow
VALID_ACTIONS = [
    "validate_account",
    "get_account_balance",
    "withdraw_in_dollars",
    "withdraw_in_pesos",
    "deposit_money"
]


# Console messages
ACTION_STATUS_MSG = "Step id: '{}' - action: '{}' - result: {}"
NEXT_TARGET_MSG = """Target is now {}
-----------------------------"""
NO_NEXT_TARGET_MSG = "No next target, finishing up!"
VALIDATION_STATUS_MSG = "Validation for step id {} - field: {}, operator: {}, value: {}, result: {}"
