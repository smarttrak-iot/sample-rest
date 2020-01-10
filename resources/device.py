from flask_restful import Resource, reqparse
from models.device import DeviceModel

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


    def get(self, devId):
        device = DeviceModel.find_by_name(devId)
        if device:
            return device.json()
        return {'message': 'Item not found'}, 404

    def post(self, devId):
        if DeviceModel.find_by_name(devId):
            return {'message': "A Device with devId '{}' already exists.".format(devId)}, 400

        data = Device.parser.parse_args()

        device = DeviceModel(devId, data['power'],data['voltage'],data['current'])

        try:
            device.save_to_db()
        except:
            return {"message": "An error occurred inserting the device data."}, 500

        return device.json(), 201


    def put(self, devId):
        data = Device.parser.parse_args()

        device = DeviceModel.find_by_name(devId)

        if device is None:
            device = DeviceModel(devId, data['power'],data['voltage'],data['current'])
        else:
            device.power = data['power']
            device.voltage = data['voltage']
            device.current = data['current']

        device.save_to_db()

        return device.json()


class DeviceList(Resource):
    def get(self):
        return {'devices': [x.json() for x in DeviceModel.query.all()]}
