"""
Decorators file

author: Diego Arango - @darango91
"""

from flask import request
from functools import wraps

from src.exceptions import BadFormattedWorkflow


def validate_workflow(function=None):
    """
    Decorator to validate the workflow base structure
    containing trigger or steps
    :param function: request (post)
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        if request.json is not None:
            if request.json.get("trigger"):
                return function(*args, **kwargs)
            elif request.json.get("steps"):
                steps = request.json.get("steps")
                for step in steps:
                    if step.get("id") == "start":
                        return function(*args, **kwargs)
                raise BadFormattedWorkflow
            else:
                raise BadFormattedWorkflow
        else:
            raise BadFormattedWorkflow

    return wrapper
