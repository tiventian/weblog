import uuid

from sqlalchemy import text

from database.mysql import db


def uuid_generator():
    _uuid = uuid.uuid1()
    _uuid_bin = bytes.fromhex(str(_uuid)[14:18] + str(_uuid)[9:13] + str(_uuid)[0:8] + str(_uuid)[18:].replace('-', ''))
    return _uuid_bin


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.BINARY(16), primary_key=True, default=uuid_generator,
                   server_default=text('(uuid_to_bin(uuid(),1))'))
    uuid = db.Column(db.String(36), nullable=True, server_default=text('(bin_to_uuid(id))'))
    name = db.Column(db.String(64), nullable=False, unique=True)
    create_time = db.Column(db.DateTime(), server_default=text('CURRENT_TIMESTAMP'))
    modify_time = db.Column(db.DateTime(), server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, name):
        super().__init__()
        self.name = name
