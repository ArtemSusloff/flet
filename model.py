from peewee import *
from playhouse.shortcuts import model_to_dict

db = SqliteDatabase("database.db")

test_dict = {'timestamp': '2024-06-09T07:12:08.498z',
             'eventId': '233AB810-0302-0000-0865-23A700A47DCF',
             'eventType': 'TransferAccepted',
             'eventSource': '/ru/regions/volga2/centers/samara443300/stations/reksoft01/sorters/bps01/session',
             'sorterId': '/ru/regions/volga2/centers/samara443300/stations/reksoft01/sorters/bps01',
             'sessionId': '6a01ac24-e8b4-42a2-8136-d02e368245f9',
             'sessionName': 'конвейер 1',
             'exits': '/ru/regions/volga2/centers/samara443300/stations/reksoft01/sorters/bps01/exits/exitGarbage',
             'internalId': '80323',
             'iteration': 1}


class BaseModel(Model):
    class Meta:
        database = db


def check_dict(checked_dict, key):
    if key in checked_dict:
        return checked_dict[key]
    else:
        return ""


class SmabLog(BaseModel):
    id = PrimaryKeyField(null=False)
    timeStamp = TextField()
    eventId = TextField()
    eventType = TextField()
    eventSource = TextField()
    sessionId = TextField()
    sessionName = TextField()
    exits = TextField()
    exitState = TextField()
    reason = TextField()
    exitId = TextField()
    exitType = TextField()
    internalId = TextField()
    iteration = TextField()
    detectorSources = TextField()
    barcode = TextField()
    height = TextField()
    length = TextField()
    weight = TextField()
    width = TextField()
    code = TextField()

    class Meta:
        db_table = "SmabLog"

    def add_record(self, data_dict):
        self.create(
            timeStamp=check_dict(data_dict, "timestamp"),
            eventId=check_dict(data_dict, "eventId"),
            eventType=check_dict(data_dict, "eventType"),
            eventSource=check_dict(data_dict, "eventSource"),
            sessionId=check_dict(data_dict, "sessionId"),
            sessionName=check_dict(data_dict, "sessionName"),
            exitState=check_dict(data_dict, "exitState"),
            exits=check_dict(data_dict, "exits"),
            reason=check_dict(data_dict, 'reason'),
            exitId=check_dict(data_dict, 'exitId'),
            exitType=check_dict(data_dict, "exitType"),
            internalId=check_dict(data_dict, "internalId"),
            iteration=str(check_dict(data_dict, "iteration")),
            detectorSources=check_dict(data_dict, "detectorSources"),
            barcode=check_dict(data_dict, "barcode"),
            height=check_dict(data_dict, "height"),
            length=check_dict(data_dict, "length"),
            weight=check_dict(data_dict, "weight"),
            width=check_dict(data_dict, "width"),
            code=check_dict(data_dict, "code"),
        )

    def get_table(self):
        return [model_to_dict(el) for el in self.select()]

    def get_headers(self):
        return self._meta.columns.keys()

# test = SmabLog()

#
# for el in test.get_table():
#     for key in el.values():
#         print(key)
