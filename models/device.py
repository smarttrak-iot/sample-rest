from db import db

class DeviceModel(db.Model):
    __tablename__ = 'devices'

    devId = db.Column(db.String(20), primary_key=True)
    power = db.Column(db.Float(precision=2))
    voltage = db.Column(db.Float(precision=2))
    current = db.Column(db.Float(precision=2))

    def __init__(self, devId,power,voltage,current):
        self.devId = devId
        self.power = power
        self.voltage = voltage
        self.current = current

    def json(self):
        return {'devId': self.devId,'power': self.power,'voltage': self.voltage,'current': self.current}

    @classmethod
    def find_by_name(cls, devId):
        return cls.query.filter_by(devId=devId).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
