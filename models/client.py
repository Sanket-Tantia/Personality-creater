import uuid
from Database import Database
class Client(object):

    def __init__(self,name,email,_id=None):
        self.name = name
        self.email = email
        self._id = uuid.uuid4().hex if id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='client',data=self.json())

    def json(self):
        return {
            '_id':self._id,
            'email':self.email,
            'name':self.name
        }

    @classmethod
    def getClient(cls,email):
        client =  Database.find_one(collection='client',query={'email':email})
        return cls(**client)

    @classmethod
    def getKeywordsByClient(cls,email):
        return [cls(**keyword) for keyword in Database.find(collection='keywords',query={'email':email})]

    @classmethod
    def getRecordByEmail(cls, email):
        return [cls(**recordHistory) for recordHistory in Database.find(collection='history', query={'email': email})]