from flask import make_response, request
from flask_restful import Resource


from db import session
from model import UserModel
from schema import UserSchema


class UserEndpoint(Resource):
    def get(self):
        expression = dict(request.args.items())

        user_model = UserModel()

        users = user_model.get_by_id(expression)

        user_jsons = user_model.jsonify(UserSchema, users, many=True)

        return make_response({"users": user_jsons}, 200)

    def post(self):
        user = request.get_json()

        new_user = UserModel(user)

        session.add(new_user)

        session.commit()

        user_schema = UserSchema()

        user_json = user_schema.dump(new_user)

        return make_response(user_json, 201)

    def put(self):
        user = request.get_json()

        new_user = UserModel(user)

        session.update(new_user)

        session.commit()

        user_schema = UserSchema()

        user_json = user_schema.dump(user)

        return make_response(user_json, 200)

    def delete(self):

        return make_response({}, 204)
