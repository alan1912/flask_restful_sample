from flask_restful import Resource


class WelcomeList(Resource):

    def get(self):
        return {"message": "GET List success!"}

    def post(self):
        return {"message": "POST is success!"}


class Welcome(Resource):

    def get(self, pk):
        return {"message": "GET " + pk + " success!"}
    
    def put(self, pk):
        return {"message": "PUT " + pk + " is success!"}

    def delete(self, pk):
        return {"message": "DELETE " + pk + " is success!"}
