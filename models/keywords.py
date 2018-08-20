import uuid
from Database import Database
class Keywords(object):

    def __init__(self,client_id,value,start_date,end_date,_id=None):
        self.client_id = client_id
        self.value = value
        self.start_date = start_date
        self.end_date = end_date
        self._id = uuid.uuid4().hex if id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='keywords',data=self.json())

    def json(self):
        return {
            'client_id': self.client_id,
            'value':self.value,
            'start_date': self.start_date,
            'end_date': self.end_date,
            '_id':self._id
        }

    @classmethod
    def getKeywordByDate(cls,start_date,end_date):
         keyword = Database.find_one(collection='keywords',query={'start_date':start_date,'end_date':end_date})
         return cls(**keyword)