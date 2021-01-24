"""
API exceptions file

author: Diego Arango - @darango91
"""

from flask_restful import HTTPException


class BadFormattedWorkflow(HTTPException):
    code = 400
    description = "The workflow is bad formatted"


class AccountNotFound(HTTPException):
    code = 404
    description = "The account was not found"
