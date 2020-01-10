from db import db

class DeviceModel(db.Model):
    __tablename__ = 'devices'

    name = db.Column(db.String(20), primary_key=True)
    power = db.Column(db.Float(precision=2))
    voltage = db.Column(db.Float(precision=2))
    current = db.Column(db.Float(precision=2))

    def __init__(self, name,power,voltage,current):
        self.name = name
        self.power = power
        self.voltage = voltage
        self.current = current

    def json(self):
        return {'name': self.name,'power': self.power,'voltage': self.voltage,'current': self.current}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
