from peewee import *

from database.mysql import pool_mysql, uuid_generator


class Base(pool_mysql.Model):
    id = BinaryUUIDField(default=uuid_generator, primary_key=True)
    uid = CharField(max_length=36, constraints=[SQL('DEFAULT (BIN_TO_UUID(`id`, true))')])
    name = CharField(max_length=32, unique=True)
    status = FixedCharField(max_length=1, choices=(('N', 'Normal'), ('H', 'Hide'), ('P', 'Publish')))
    create_time = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    modify_time = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')])

    class Meta:
        database = pool_mysql.database
