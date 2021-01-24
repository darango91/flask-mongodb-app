
INITIAL_DATA = [
  {
    "user_id": "105398891",
    "pin": 2090,
    "balance": 100001
  },
  {
    "user_id": "105398892",
    "pin": 1111,
    "balance": 100000
  },
  {
    "user_id": "105398893",
    "pin": 2323,
    "balance": 250000
  },
  {
    "user_id": "105398894",
    "pin": 6598,
    "balance": 350100
  },
  {
    "user_id": "105398895",
    "pin": 8526,
    "balance": 50000
  },
  {
    "user_id": "105398896",
    "pin": 9658,
    "balance": 110000
  }
]


TEST_WORKFLOW = {
  "trigger": {
    "params": {
      "user_id": "105398891",
      "pin": 2090
    },
    "transitions": [
      {
        "target": "validate_account",
        "condition": []
      }
    ],
    "id": "start"
  },
  "steps": [
    {
      "id": "validate_account",
      "params": {
        "user_id": {"from_id": "start", "param_id": "user_id"},
        "pin": {"from_id": "start", "param_id": "pin"}
      },
      "action": "validate_account",
      "transitions": []
    }
  ]
}
