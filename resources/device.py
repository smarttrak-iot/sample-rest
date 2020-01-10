from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Device(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('power',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('voltage',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('current',
        type=float,
        required=True,
        help="This field cannot be left blank!"
        )


    def get(self, name):
        device = DeviceModel.find_by_name(name)
        if device:
            return device.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if DeviceModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Device.parser.parse_args()

        device = ItemModel(name, data['power'],data['voltage'],data['current'])

        try:
            device.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return device.json(), 201


    def put(self, name):
        data = Device.parser.parse_args()

        device = DeviceModel.find_by_name(name)

        if device is None:
            device = DeviceModel(name, data['power'],data['voltage'],data['current'])
        else:
            device.power = data['power']
            device.voltage = data['voltage']
            device.current = data['current']

        device.save_to_db()

        return device.json()


class DeviceList(Resource):
    def get(self):
        return {'devices': [x.json() for x in DeviceModel.query.all()]}
