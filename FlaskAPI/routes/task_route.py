from flask import Blueprint
from flask_restful import Api

from endpoint import TaskEndpoint

task_route = Blueprint("task_route", __name__)

api = Api(task_route)

api.add_resource(TaskEndpoint,"/tasks", "/tasks/<int:task_id>")