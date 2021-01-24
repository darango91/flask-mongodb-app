"""
Flask routes file

Author: Diego Arango - @darango91
"""
from bson import json_util
from flask import request, Response

from src.constants import API_TEST_TEXT
from src.decorators import validate_workflow
from src.workflow_helper import WorkflowHelper


def configure_routes(app, mongo):
    @app.route("/workflows", methods=["POST"])
    @validate_workflow
    def upload_workflow():
        """
        Endpoint to upload a workflow and be executed
        :return:
        """
        workflow = request.json
        wh = WorkflowHelper(workflow, mongo)
        wh.process_workflow()

        return {"data": request.json}, 200

    @app.route('/accounts', methods=['POST'])
    def create_sample_accounts():
        """
        Creates given accounts inside the DB
        :return: the inserted ids
        """

        accounts = request.json
        result = mongo.db.accounts.insert_many(
            accounts
        )

        return Response(
            json_util.dumps(result.inserted_ids), mimetype='application/json'
        )

    @app.route('/test_me', methods=['GET'])
    def test_me_endpoint():
        """
        Creates given accounts inside the DB
        :return: the inserted ids
        """
        result = API_TEST_TEXT
        return {"data": result}
