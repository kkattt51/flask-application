from flask_restful import Resource

from src.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self):
        pass

    def post(self):
        pass

    def put(self, uuid):
        pass

    def delete(self, uuid):
        pass
