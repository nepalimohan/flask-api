from flask_restful import Resource

class Item(Resource):
    def get(self, name):
        return {'item': name}, 200
    
    def post(self, name):
        return {'message': f'Item {name} created'}, 201
    
    def delete(self, name):
        return {'message': f'Item {name} deleted'}, 200