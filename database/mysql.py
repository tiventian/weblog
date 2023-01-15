import uuid


def uuid_generator(_uuid=None):
    if not _uuid:
        _uuid = uuid.uuid1()
    _uuid_bin = bytes.fromhex(str(_uuid)[14:18] + str(_uuid)[9:13] + str(_uuid)[0:8] + str(_uuid)[18:].replace('-', ''))
    return _uuid_bin
