from flask_restful import Resource, reqparse

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, require=True, help="This field cannot be left blank!")
    
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item, 200
        return {'message': 'Item not found'}, 200
    
    def post(self, name):
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item) 
        return item, 201
    
    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': f'Item {name} deleted'}, 200