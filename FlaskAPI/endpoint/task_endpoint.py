from flask import make_response, request
from flask_restful import Resource


from db import session
from model import TaskModel
from schema import TaskSchema


class TaskEndpoint(Resource):
    def get(self):
        expression = dict(request.args.items())

        task_model = TaskModel()

        tasks = task_model.get_all()

        task_jsons = task_model.jsonify(TaskSchema, tasks, many=True)

        return make_response(task_jsons, 200)

    def post(self):
        task = request.get_json()

        new_task = TaskModel(task)

        session.add(new_task)

        session.commit()

        task_schema = TaskSchema()

        task_json = task_schema.dump(new_task)

        return make_response(task_json, 201)

    def put(self):
        task = request.get_json()

        new_task = TaskModel(task)

        new_task.update()

        task_schema = TaskSchema()

        task_json = task_schema.dump(task)

        return make_response(task_json, 200)
    
    def patch(self):
        task = request.get_json()

        task_model = TaskModel(task)
        
        task_model.update_status()

        return make_response({}, 200)

    def delete(self, task_id):

        task_model = TaskModel({ "id":task_id})

        task_model.delete()

        return  make_response({}, 204)
