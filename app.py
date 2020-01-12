import os

from flask import Flask, request,render_template
from flask_restful import Api

from models.device import DeviceModel
from resources.device import Device, DeviceList

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'smarttrak'
api = Api(app)

@app.route('/')
def home():

    devices = DeviceModel.query.all()
    return render_template('index.html',devices=devices)

#jwt = JWT(app, authenticate, identity)  # /auth

#api.add_resource(Store, '/store/<string:name>')
#api.add_resource(Item, '/item/<string:name>')
#api.add_resource(ItemList, '/items')
#api.add_resource(StoreList, '/stores')

app.add_resource(Device, '/device/<string:devId>')
app.add_resource(DeviceList, '/devices')

#api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
